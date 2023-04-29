# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 11:52:48 2023

@author: kevin
"""
import json
import requests 
from flask import Flask, request, render_template, flash, redirect, url_for
app = Flask(__name__)
app.config['SECRET_KEY'] = 'kihg75'




@app.route("/", methods = ('GET','POST'))
def home():
    if request.method == 'POST':
        lat = request.form['lat']
        long = request.form['long']

        if not lat:
            flash('Fill out the latitude')
        elif not long:
            flash('Fill out the longitude')
        else:
            return redirect(f'/weather?lat={lat}&long={long}') 
    return render_template("create.html")

@app.route('/weather')
def weather():
    lat = request.args.get('lat')
    long = request.args.get('long')
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid=30dba34f1ddfef698f3b3d3500666234&units=metric"
    response = requests.get(url)
    return response.json()



if __name__ == "__main__":
    app.run(host = '0.0.0.0')