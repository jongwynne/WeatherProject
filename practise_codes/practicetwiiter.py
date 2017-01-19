from twython import TwythonStreamer
import pandas as pd
from pandas import DataFrame, Series
import pickle
import datetime
cur_time_stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H")
with open(r'c:\\data\\twitter_scrape_pickle', 'rb') as p1:
    tweets = pickle.load(p1)
    frame = DataFrame(tweets)
    frame2 = frame['text']
frame2.to_csv("c:\\data\\twitter_scrape"+ cur_time_stamp +".csv", sep=',', encoding='utf-8')
#with open(r"c:\data\twitter_scrape.csv", "wb") as tw:
#    for t in tweets:
#        if 'text' in t:
#            text2 = t['text'].encode('utf-8')
#            create2 = t['created_at'].encode('utf-8')
#            tw.write(text2 + ' ' + create2 )

