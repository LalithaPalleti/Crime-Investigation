from flask import Flask, render_template, request, redirect
import json
import requests
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
import quandl
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
    data = quandl.get_table('WIKI/PRICES',
                       ticker = request.form['address'])
    p = figure(plot_width=400, plot_height=400,x_axis_type = "datetime")
    p.line(data.date,data.open,line_width = 2,legend = request.form['address'],color = 'green')
    
    script, div = components(p)
    return render_template('line.html',div=div,script=script)


if __name__ == '__main__':
  app.run(host = '0.0.0.0',port=33507,debug='true')
