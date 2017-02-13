import json

with open (r"c:\data\twitter_scrape.json", "r") as tw :
    t = json.load(tw)
    for tweet in t:
        print tweet