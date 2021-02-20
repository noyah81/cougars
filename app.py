#saved from main, but altered. If this works, this code could be incorporated into main.
import sqlite3 #left this here for now...
from datetime import datetime
import os
from flask import Flask, render_template, flash, redirect, url_for, session, logging
from flask import request
import requests
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc

app = Flask(__name__)

######################################
#### SET UP OUR SQLite DATABASE #####
####################################

# This grabs our directory
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# Connects our Flask App to our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'travelsite.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
#OMG SO IMPORTANT TO INCLUDE THIS ABOVE! Warnings up the wazoo if not here on a develoment server.

db = SQLAlchemy(app)

# API STUFF
@app.route('/stations', methods=['GET', 'POST'])
def stations():
    url = 'http://mtaapi.herokuapp.com/stations'  # the url for the stations list
    resp = requests.get(url)
    stations = resp.json()['result']  # list with dictionaries inside

    stations = sorted(stations, key=lambda d: d['name'])

    return render_template('stations.html', stations=stations)


@app.route('/traintime/<string:id>', methods=['GET', 'POST'])
def traintime(id):
    station = id
    url = 'http://mtaapi.herokuapp.com/api?id=' + station
    resp = requests.get(url)
    times = resp.json()['result']['arrivals']
    times.sort()
    unique_times = [] #comparison list.
    display_times = []#display list.
    now = datetime.now()
    #$ is a typo. % instead gives us the right values -- let's not include the seconds.
    current_time = now.strftime("%H:%M%S")
    display_time = now.strftime("%I:%M %p")
    counter = 0

    #updated formatting for times in list
    for time in times:
        #format of time is: 03:45:00
        time = time[0:5] #this takes it down to hour and minute, no more seconds.

        if time not in unique_times and not (time[0] + time[1] == '24'):
           
            if time >= current_time and counter < 10:
                unique_times.append(time) #keeps it so we can cleanly compare times

                #let's separate hours from minutes to compare for am/pm
                time = time.split(':')
                h = time[0]
                m = time[1]
                merideim = 'AM'

                if int(h) > 11: #casts as int so we can compare numbers easily
                    merideim = 'PM'
                    h = int(h)-12 #lets us subtract numbers easily

                if h == 0:
                    h = 12

                if h < 10:
                    h = f"0{h}" #keeps double integer for time display consistantcy. 
                
                ftime = f"{h}:{m} {merideim}"
                display_times.append(ftime)
                counter += 1

    name = resp.json()['result']['name']
    return render_template('traintime.html', times=display_times, name=name, current_time=display_time)


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    # home3 is for layout experimentation
    conn = sqlite3.connect('travelsite.db')
    cur = conn.cursor()
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        comment = request.form['comment']

        #sqlite language command:
        cur.execute("INSERT INTO reviews VALUES (?,?,?)", (name, location, comment))

    cur.execute("SELECT * from reviews")
    items = cur.fetchall()
    conn.commit()
    conn.close()
    return render_template("home.html", items=items)

@app.route("/madisonsquare")
def madisonsquare():
    return render_template("madisonsquare.html")


@app.route("/liberty")
def liberty():
    return render_template("liberty.html")


@app.route("/time")
def time():
    return render_template("time.html")


@app.route("/central")
def central():
    return render_template("central.html")


@app.route("/museum")
def museum():
    return render_template("museum.html")


@app.route("/statue")
def statue():
    return render_template("statue.html")

@app.route("/empire")
def empire():
    return render_template("empire.html")


@app.route("/Wallstreetstation")
def wallstreetstation():
    return render_template("Wallstreetstation.html")


@app.route("/easter")
def easter():
    return render_template("easter.html")

@app.route("/iam")
def iam():
    return render_template("iam.html")


@app.route("/ticket1")
def ticket1():
    return render_template("ticket1.html")


@app.route("/location")
@app.route("/location/<string:url>")
def location(url=''): 
#this makes it so that if there's no location, it still outputs something to the page
    if url == '':
        #have it spit out locations.html which has all the locations on it and choose it.
        return render_template('no_loc.html')
    else:
        conn = sqlite3.connect('travelsite.db')
        #create a cursor
        cur = conn.cursor()
        cur.execute("SELECT * from locations WHERE url = (?)", (url,))
        location = cur.fetchone()
        conn.commit()
        
        title=location[1]

        cur.execute("SELECT * from reviews WHERE location = (?)", (title,))
        items = cur.fetchall()
        conn.commit()
        conn.close()

        station_list = location[6].split(',')

    return render_template("location.html", url=url, title=title, image=location[3], body=location[4], gmapLink=location[5], stations=station_list, body_class='location', items=items)



@app.route('/dashboard')
#@is_logged_in #decorator will come later
def dashboard():

    return render_template('dashboard.html')


# RUNv
if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port='5000')
