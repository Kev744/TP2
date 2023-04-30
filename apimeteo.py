# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 11:52:48 2023

@author: kevin
"""
import requests
import os
from flask import Flask, request, render_template, flash, redirect
app = Flask(__name__)
app.secret_key = 'df0331cefc6c2b9a5d0208a726a5d1c0fd37324feba25506'




@app.route("/", methods = ('GET','POST'))
def home():
    if request.method == 'POST':
        lat = request.form['lat']
        long = request.form['long']

        if not lat:
            flash('Fill out the latitude')
        elif not(lat.replace(".","",1).isdigit()) :
            flash("Correct the field lat in correct format")
        elif not long:
            flash('Fill out the longitude')
        elif not(long.replace(".","",1).isdigit()) :
            flash("Correct the field long in correct format")
        else:
            return redirect(f'/weather?lat={lat}&long={long}') 
    return render_template("create.html")

@app.route('/weather')
def weather():
    lat = request.args.get('lat')
    long = request.args.get('long')
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()



if __name__ == "__main__":
    api_key = os.environ["API_KEY"]
    app.run(host = '0.0.0.0')
    
