import sqlite3
from datetime import datetime
import requests # this needs to be here in order to get data from forms. And it is requests not request
from flask import Flask, render_template
from flask import request

app = Flask(__name__)


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
    unique_times = []
    now = datetime.now()
    current_time = now.strftime("%H:$M:$S")
    counter = 0

    for time in times:
        if time not in unique_times and not (time[0] + time[1] == '24'):
            if time >= current_time and counter < 10:
                unique_times.append(time)
                counter += 1

    times = unique_times
    name = resp.json()['result']['name']
    return render_template('traintime.html', times=times, name=name, current_time=current_time)


# removed this code so that both the root and the home show the same info
# def root():
#     return render_template("base.html")


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    # home2 is for layout experimentation
    conn = sqlite3.connect('travelsite.db')
    cur = conn.cursor()
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        comment = request.form['comment']
        # print(name)
        # print(location)
        # print(comment)
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


# RUNv
if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port='5000')
