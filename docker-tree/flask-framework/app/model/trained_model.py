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
import pickle

def buildModel():
    parsed_dataframe = get_data()
    print parsed_dataframe.head()
    sys.stdout.flush()
    #address = str(request.form['address'])
    address = '1912 Pike Place Seattle, WA 98101'
    print address
    sys.stdout.flush()
    Quality = ['Drugs','Liquor']
    Property = ['Property Crime','Theft','Theft of Vehicle','Theft from Vehicle']
    Violent = ['Assualt','Robbery','Breaking & Entering']
    data =  getcrimesby_tier(address,parsed_dataframe,Quality)
    print data
    sys.stdout.flush()
    forecast_model(data)

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
    locator = Nominatim()
    parsed_address = locator.geocode(address)
    print parsed_address
    sys.stdout.flush()
    input_cordinates = (parsed_address.latitude,parsed_address.longitude)
    for i,r in data.iterrows():
	#location = locator.geocode(r)
        coordinates  = (r.latitude,r.longitude)
        distance_miles = great_circle(input_cordinates,coordinates).miles
	print distance_miles
	sys.stdout.flush()
        days = (r.incident_datetime.now().date() - r.incident_datetime.date()).days
        if (distance_miles < 20 and days < 300):
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
    fbprophet_model_pkl_filename = 'fbprophet_model.pkl'
    fbprophet_model_pkl = open(fbprophet_model_pkl_filename, 'wb')
    pickle.dump(model, fbprophet_model_pkl)
    fbprophet_model_pkl.close()

if __name__ == '__main__':
     	buildModel()
