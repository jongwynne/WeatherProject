import json
import urllib
import pandas as pd
import pickle
import datetime as dt
from pandas import DataFrame, Series

url = 'http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/352409?res=3hourly&key=1048a1c2-d53f-4e66-b614-48740f6fa09f'
response = urllib.urlopen(url)
data = json.load(response)

with open('C:\\Users\\Student30\\Documents\\Met Data project\\met data files\\varcleanmetoffice', 'rb') as p1:
    frame = pickle.load(p1)

origin = data.get('SiteRep', 'none').get('DV', 'none').get('dataDate', 'none')
y = int(origin[0:4])
m = int(origin[5:7])
d = int(origin[8:10])
h = int(origin[11:13])
origin = dt.datetime(y,m,d,h,0,0)
period = data.get('SiteRep', 'none').get('DV', 'none').get('Location').get('Period', 'none')
inctime = dt.datetime(y,m,d,h-3,0,0)
listy = []
for i in period:
    rep = i.get('Rep')
    for j in rep:
        inctime += dt.timedelta(hours = 3)
        listy = [inctime, origin, j.get('$'), j.get('D'), j.get('F'), j.get('G'), j.get('H'), j.get('Pp'), j.get('S'), j.get('T'), j.get('U'), j.get('V'), j.get('W')]
        frame = frame.append(Series(listy, index = ['Forecast Time','origin','UTC', 'Wind Direction', 'Degrees Celsius', 'Wind Gust (MPH)', 'Humidity', 'Precipitation', 'Wind Speed', 'Screen Temp', 'UV index', 'Visibility', 'Weather']), ignore_index = True)

with open('C:\\Users\\Student30\\Documents\\Met Data project\\met data files\\varcleanmetoffice', 'wb') as p2:
    pickle.dump(frame, p2)