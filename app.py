
from flask import Flask, jsonify, render_template, request, g


stop_times = open("google_transit/stop_times.txt", "r+")
stops_info = open("google_transit/stops.txt", "r+")


# Create stops
stops = {}
for line in stops_info:
    # print line
    data = line.split(",")
    id = data[0]
    name = data[2]
    lat = data[4]
    lon = data[5]
    stop = {'name' : name, 'lat': lat, 'lon': lon}
    stops[id] = stop
# print type(stops)

# Create arrivals
ids = []
arrivals = {}
for line in stop_times:
    data = line.split(",")
    time = data[1]
    id = data[3]
    if id not in ids:
        ids.append(id)
    arrivals.setdefault(id,[]).append(time)
# print 'len(ids)', len(ids)


data = {}
for id in ids:
    data[id] = {'name' : stops[id]['name'], 'lat': stops[id]['lat'], 'lon': stops[id]['lon'], 'arrivals': arrivals[id]}




