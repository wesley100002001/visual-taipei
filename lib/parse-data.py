# -*- coding: utf-8 -*-
import json
import csv
from pprint import pprint

with open('../raw/bus.json') as data_file:
    bus = json.load(data_file)

output = []
bus_stop_dict = {}
output.append(['id', 'latitude', 'longitude', 'name', 'type', 'color', 'url'])

for i in range(len(bus['features'])):
    if bus['features'][i]['properties']['bsm_chines'].encode('utf-8') not in bus_stop_dict:
        bus_stop_dict[bus['features'][i]['properties']['bsm_chines'].encode('utf-8')] = [
            i + 1,
            bus['features'][i]['geometry']['coordinates'][1],
            bus['features'][i]['geometry']['coordinates'][0],
            bus['features'][i]['properties']['bsm_chines'].encode('utf-8'),
            'Bus',
            609128,
            'http://www.google.com.tw'
        ]

for value in bus_stop_dict.itervalues():
    output.append(value)

# https://github.com/repeat/taipei-metro-stations/blob/master/taipei.csv
mrt = open('../raw/mrt.csv')
for row in csv.reader(mrt):
    output.append([
        row[0],
        row[6],
        row[7],
        row[1],
        'MRT',
        '00529d',
        'http://www.google.com.tw'
    ])

output_file = open('../data/transportation.csv', 'w')
csvWriter = csv.writer(output_file)
csvWriter.writerows(output)
output_file.close()
