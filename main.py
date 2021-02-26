import sqlite3 #left this here for now... will move away from that and remove if there is time
from datetime import datetime
import os
from flask import Flask,request,render_template, flash, redirect, url_for, session,logging,flash,abort
from flask_login import login_user,login_required,logout_user,LoginManager
from forms import LoginForm, RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash
import requests # this needs to be here in order to get data from forms. And it is requests not request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from flask_migrate import Migrate
from flask_login import UserMixin

app = Flask(__name__)

# Create a login manager object
login_manager = LoginManager()

######################################
#### SET UP OUR SQLite DATABASE #####
####################################

# This grabs our directory
basedir = os.path.abspath(os.path.dirname(__file__))


#maintains session
app.config['SECRET_KEY'] = 'mysecretkey'
# Connects our Flask App to our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'travelsite.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#OMG SO IMPORTANT TO INCLUDE THIS ABOVE! Warnings up the wazoo if not here on a develoment server.

db = SQLAlchemy(app)
Migrate(app,db)

# We can now pass in our app to the login manager
login_manager.init_app(app)

# Tell users what view to go to when they need to login.
login_manager.login_view = "login"

######################################
############## MODELS ###############
####################################
# The user_loader decorator allows flask-login to load the current user
# and grab their id.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):

    # Create a table in the db
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        # https://stackoverflow.com/questions/23432478/flask-generate-password-hash-not-constant-output
        return check_password_hash(self.password_hash,password)


class Review(db.Model):
    # Create a table in the db
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))
    location = db.Column(db.Text)
    comments = db.Column(db.Text)

    def __init__(self, name, location, comments):
        self.name = name
        self.location = location
        self.comments = comments
    #repr is a representation of the object.
    def __repr__(self):
        #f"..." is string formatting.
        return f"comment data: {self.name, self.location, self.comments}"


class Location(db.Model):
    # Create a table in the db
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.Text, unique=True, nullable=False)
    url = db.Column(db.Text, unique=True, nullable=False)
    image = db.Column(db.Text, unique=True, nullable=False)
    body = db.Column(db.Text, unique=False, nullable=False)
    gmap_link = db.Column(db.Text, unique=True, nullable=False)
    stations = db.Column(db.Text, unique=False, nullable=False) #should be csv of stations, no spaces between.

    def __init__(self, name, location, comments):
        self.name = name
        self.location = location
        self.comments = comments
    #repr is a representation of the object.
    def __repr__(self):
        #f"..." is string formatting.
        return f"location: {self.title, self.location, self.url, self.image, self.body, self.gmap_link, self.stations}"


db.create_all();

##### End Models ######

######################################
############## VIEWS ################
####################################

@app.route('/logout')
@login_required
def logout():
    logout_user()
    #flash('You logged out!') #not using flash yet....
    return redirect(url_for('home'))


@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        # Grab the user from our User Models table
        user = User.query.filter_by(email=form.email.data).first()

        # Check that the user was supplied and the password is right
        # The verify_password method comes from the User object
        # https://stackoverflow.com/questions/2209755/python-operation-vs-is-not

        if user.check_password(form.password.data) and user is not None:
            #Log in the user

            login_user(user)
            print('Logged in successfully.')
            #flash('Logged in successfully.')#not using flash yet...

            # If a user was trying to visit a page that requires a login
            # flask saves that URL as 'next'.
            next = request.args.get('next')

            # So let's now check if that next exists, otherwise we'll go to
            # the dashboard.
            if next == None or not next[0]=='/':
                next = url_for('dashboard') #redirect to dashboard when successful.

            return redirect(next)
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    #added this bit so you can register users as long as they have the special code.
    urlParam = ''
    urlParam = request.args.get('password', '')

    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        #flash('Thanks for registering! Now you can login!') #not using flash yet....
        return redirect(url_for('login'))
    return render_template('register.html', form=form, page_pass=urlParam)


############# end login/register stuff ###################


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
    cur.execute("SELECT title,url,image from locations")
    locations = cur.fetchall()
    conn.commit()

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
    return render_template("home.html", items=items, locations=locations)

'''
these routes can be eliminated in favor of the new locations routes, since they are in the database in the locations table:

@app.route("/madisonsquare")
def madisonsquare():
    return render_template("madisonsquare.html")

@app.route("/liberty")
def liberty():
    return render_template("liberty.html")

@app.route("/museum")
def museum():
    return render_template("museum.html")

@app.route("/statue")
def statue():
    return render_template("statue.html")

@app.route("/empire")
def empire():
    return render_template("empire.html")
@app.route("/time")
def time():
    return render_template("time.html")
'''

@app.route("/central")
def central():
    return render_template("central.html")

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

@app.route("/location") #gets all locations
@app.route("/location/") #gets all locations
@app.route("/location/<string:url>") #gets specific location
def location(url=''):
    conn = sqlite3.connect('travelsite.db')
    #create a cursor
    cur = conn.cursor()
    #this makes it so that if there's no location, it still outputs something to the page
    if url == '':
        cur.execute("SELECT title,url,image from locations")
        locations = cur.fetchall()
        conn.commit()
        #have it spit out locations.html which has all the locations on it and choose it.
        return render_template('locations.html', body_class='location', locations=locations)
    else:
        cur.execute("SELECT * from locations WHERE url = (?)", (url,))
        location = cur.fetchone()
        print(location) #comes back as None when there is no result.
        if location is None:
            title=''
            url=url,
            image=''
            body=''
            gmapLink=''
            stations=''
            body_class='no-location'
            items=''
            isText=''
            return render_template("no_location.html", body_class=body_class )
        else:
            #we have data from the database on this location
            title=location[1]
            image=location[3]
            body=location[4]
            gmapLink=location[5]
            body_class='location'

            cur.execute("SELECT * from reviews WHERE location = (?)", (title,))
            items = cur.fetchall()
            conn.commit()
            conn.close()

            station_list = []
            #api
            stop_list = location[6].split(',')

            for stop in stop_list:
                url = 'http://mtaapi.herokuapp.com/stop?id='+stop  # the url for the stations
                stop_char = stop[-1]
                if stop_char == 'N':
                    stop_char = 'Northbound'
                elif stop_char == 'S':
                    stop_char = 'Southbound'
                elif stop_char == 'E':
                    stop_char = 'Eastbound'
                elif stop_char == 'W':
                    stop_char = 'Westbound'

                resp = requests.get(url)
                stop_data = resp.json()['result']
                if stop_data == "key not found":
                    station_list = location[6]
                else:
                    stop_dict = {'name':stop_data['name'],'direction':stop_char, 'stop_id': stop, }
                    station_list.append(stop_dict)


                stations=station_list

                if isinstance(station_list, str):
                    isText = True
                else:
                    isText = False

    return render_template("location.html", url=url, title=title, image=image, body=body, gmapLink=gmapLink, stations=stations, body_class='location', items=items, isText=isText)


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

# RUNv
if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port='5000')