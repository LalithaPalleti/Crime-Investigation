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
import seaborn as sns
import pystan
#get_ipython().magic(u'matplotlib inline')
#plt.rcParams['figure.figsize']=(20,10)
#plt.style.use('ggplot')

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
    #parsed_dataframe = get_data()
    #address = request.form['address']
   # data =  getcrimesby_tier(address,Quality)
    #forecast_model(data)    
    data = quandl.get_table('WIKI:`/PRICES',
                       ticker = request.form['address'])
    p = figure(plot_width=400, plot_height=400,x_axis_type = "datetime")
    p.line(data.date,data.open,line_width = 2,legend = request.form['address'],color = 'green')
    
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
def getcrimesby_tier(address,crime_type):
    tier = []
    dictionary = {}
    for i,r in get_data().iterrows():
        coordinates  = (r.latitude,r.longitude)
        locator = Nominatim()
        input_cordinates = (locator.geocode(address).latitude,locator.geocode(address).longitude)
        distance = great_circle(input_cordinates,coordinates).miles
        days = (r.incident_datetime.now().date() - r.incident_datetime.date()).days
        if (distance < 20 and days < 150):
            if(r.parent_incident_type in crime_type):
                if (r.incident_datetime.date()) not in dictionary:
                    dictionary[r.incident_datetime.date()] = 1
                else:
                    dictionary[r.incident_datetime.date()] = dictionary[r.incident_datetime.date()] + 1
                    
    for key ,value in dictionary.items():
        tier.append([key,value])
    tier_df = pd.DataFrame(tier,columns = ['Date','Incidents'])
    return tier_df


if __name__ == '__main__':
   app.run(host = '0.0.0.0',port=33507,debug='true')
