from flask import render_template
from restapi import restapi_bp
from models.lessons import menus
import requests

# connects default URL to a function


@restapi_bp.route('/stations',  methods=['GET', 'POST'])
def stations():
    # call to random joke web api
    url = 'mtaapi.herokuapp.com/stations'
    response = requests.get(url)
    # formatting variables from return
    time = response.json()[0]['id']
    name = response.json()[0]['name']
    return render_template("restapi/stations.html", menus=menus,  time=time, name=name)

