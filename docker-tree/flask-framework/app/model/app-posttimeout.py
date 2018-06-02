from flask import Flask, render_template, request, redirect
import json
import requests
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
import quandl
from geopy.geocoders import Nominatim
from geopy.distance import vincenty
from geopy.distance import great_circle
from geopy.exc import GeocoderTimedOut
from datetime import datetime
#import matplotlib.pyplot as plt
import numpy as np
from fbprophet import Prophet
#import seaborn as sns
import pystan
#get_ipython().magic(u'matplotlib inline')
#plt.rcParams['figure.figsize']=(20,10)
#plt.style.use('ggplot')
import sys

quandl.ApiConfig.api_key = 'hMy3FpyQh61czyanLwbC'
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/plot',methods = ['GET','POST'])
def plot():
    parsed_dataframe = get_data()
    print parsed_dataframe.head()
    sys.stdout.flush()
    address = str(request.form['address'])
    print address
    sys.stdout.flush()
    Quality = ['Drugs','Liquor']
    Property = ['Property Crime','Theft','Theft of Vehicle','Theft from Vehicle']
    Violent = ['Assualt','Robbery','Breaking & Entering']
    data =  getcrimesby_tier(address,parsed_dataframe,Quality)
    print data
    sys.stdout.flush()
    #script, div = forecast_model(data)    
    #  data = quandl.get_table('WIKI/PRICES',
       #                ticker = request.form['ticker'])
    p = figure(plot_width=400, plot_height=400,x_axis_type = "datetime")
    #p.line(data.date,data.open,line_width = 2,legend = request.form['ticker'],color = 'green')
    
    script, div = components(p)
    return render_template('line.html',div=div,script=script)

def get_data():
	filename = "https://moto.data.socrata.com/resource/4h35-4mtu.json?$$app_token=SGf4MCedoqeOfxb7GPiMDUdf7"
	response = requests.get(filename)
	data = response.json()
#Data is represented in the form of Data frame 
	df = pd.DataFrame(data)

#converting data types 
	df['incident_datetime'] = pd.to_datetime(df['incident_datetime'])
	df['created_at'] = pd.to_datetime(df['created_at'])
	df['updated_at'] = pd.to_datetime(df['updated_at'])

#cleaning erroneous data:
	parsed_df = df[df['created_at'] >= df['incident_datetime']]			
	return parsed_df

#get crimes by tier
def getcrimesby_tier(address,data,crime_type):
    tier = []
    dictionary = {}
    for i,r in data.iterrows():
	#location = locator.geocode(r)
        coordinates  = (r.latitude,r.longitude)
        locator = Nominatim()
	parsed_address = locator.geocode(address)
	print parsed_address
	sys.stdout.flush()
        input_cordinates = (parsed_address.latitude,parsed_address.longitude)
        distance_miles = great_circle(input_cordinates,coordinates).miles
	print distance_miles
	sys.stdout.flush()
        days = (r.incident_datetime.now().date() - r.incident_datetime.date()).days
        if (distance_miles < 20 and days < 150):
            if(r.parent_incident_type in crime_type):
                if (r.incident_datetime.date()) not in dictionary:
                    dictionary[r.incident_datetime.date()] = 1
                else:
                    dictionary[r.incident_datetime.date()] = dictionary[r.incident_datetime.date()] + 1
                    
    for key ,value in dictionary.items():
        tier.append([key,value])
    tier_df = pd.DataFrame(tier,columns = ['Date','Incidents'])
    return tier_df

# create forecasting model
def forecast_model(df):
    #Preparing data for Prophet
    df1 = df.reset_index()
    #for prophet to work, columns should be in teh format ds and y
    df1 = df1.rename(columns={'Date':'ds', 'Incidents':'y'})
    #drawing a plot with ds and y
    #df1.set_index('ds').y.plot()
    #converting normal values to log values using numpy's log function to remove anamolies
    df1['y'] = np.log(df1['y'])
    #df1.set_index('ds').y.plot()
    #Running Prophet
    model = Prophet(yearly_seasonality =True,weekly_seasonality= True,daily_seasonality = True)
    model.fit(df1);
    #i want to forecast 6 months of data, so am using periods = 6 and "m" means month
    future = model.make_future_dataframe(periods= 6, freq = "m")
    #to forecast this future data we have to run it through prophet model
    forecast = model.predict(future)
    # we are interested only in yhat, yhat_lower, yhat_upper values
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
    #this function plot gives actual data in black dots and forecast data in blue lines
    #model.plot(forecast);
    return plotting(forecast)

def plotting(prediction): # pylint: disable=C0103
    #plots two lines given by prediction and df
    fig = figure(x_axis_type="datetime")
    fig.line(prediction['ds'].values,
             prediction['yhat'].values,
             line_color='red')
    #fig.line(df['ds'].values, df['y'].values)

    script, div = components(fig)

    return script, div

if __name__ == '__main__':
   app.run(host = '0.0.0.0',port=33507,debug='true')
