from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def root():
  return render_template("base.html")

@app.route("/madisonsquare")
def madisonsquare():
    return render_template("madisonsquare.html")

@app.route("/Wallstreetstation")
def Wallstreetstation():
    return render_template("Wallstreetstation.html")

# Given station, returns all info about that station
@app.route('/api')
def api():
    id = request.args.get('id', 0, type=str)
    print 'request for id', id
    try:
        res = data[id]
        response = jsonify(result=res)
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
    except KeyError:
        print 'Invalid Key'
        response = jsonify(result='key not found')
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

 Given time, returns all stations where train stops at that time
@app.route('/times')
def times():
    if len(request.args) != 2:
        response = jsonify(result='must specify hour and minute')
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
    else:
        hour = request.args.get('hour', 0, type=str)
        minute = request.args.get('minute', 0, type=str)
        # print 'request for hour and min', hour, minute
        i = 0
        results = []
        for key in data:
            arrivals = data[key]['arrivals']
            for arrival in arrivals:
                a = arrival.split(":")
                if a[0] == hour and a[1] == minute:
                    result = {'id': key, 'name': data[key]['name'], 'lat': data[key]['lat'], 'lon': data[key]['lon'], 'arrival': arrival}
                    results.append(result)
        response = jsonify(result=results)
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

# Provide ids for all stations
@app.route('/stations')
def stations():
    stations = []
    for id in ids:
        station = {'id': id, 'name': data[id]['name']}
        stations.append(station)
    response = jsonify(result=stations[1:])
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/stop')
def station():
    try:
        req = request.args.get('id', 0, type=str)
        res = {'name': data[req]['name'], 'lat': data[req]['lat'], 'lon': data[req]['lon']}
        response = jsonify(result=res)
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
    except KeyError:
        response = jsonify(result='key not found')
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1',port='3000')
