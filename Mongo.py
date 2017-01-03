import json
import urllib2
import pymongo

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.sugarkube
twittercol = db.twitter

twitter_page = open(r"c:\\data\\twitter_scrapedatamining2.csv")

parsed = json.loads(twitter_page.read())

for item in parsed:
    twittercol.insert_one(item)
