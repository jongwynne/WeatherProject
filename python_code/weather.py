import pandas as pd
import datetime

locations = [352409]     # this is for just "London"
weather_url_p1 = 'http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/'
weather_url_p2 = '?res=3hourly&key=8057bc82-1b58-4b7d-a54e-c7d275935300'
for loc in locations:
    raw_weather = pd.read_json(weather_url_p1 + str(loc) + weather_url_p2)
    cur_time_stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H")
    raw_weather.to_json('C:\\GIT\\Weather\\forecast\\' + cur_time_stamp + '-id-' + str(loc) + '-frc.json')