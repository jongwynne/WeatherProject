from twython import TwythonStreamer
import pickle
from pandas import DataFrame, Series
import datetime

tweets = []
CONSUMER_KEY = 'Cm099MoBTeVX1j1ZXsi0c2hZP'
CONSUMER_SECRET = 'Uqmb4xnVjnMw9h05HzHKxXcTdpNa3aH0cy9AIaJseIgmLDN9Fa'
ACCESS_TOKEN = '803229807504986114-0woyC72IkNnUWN7KJxnqYSp4WI4pdq7'
ACCESS_TOKEN_SECRET = 'eC1EJRIZClscMoVMXb8xIx9t0OgiwyNozNsqewlsFt9r2'

cur_time_stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H")


class MyStreamer(TwythonStreamer):

    def on_success(self, data):
            tweets.append(data)
            print len(tweets)

            if len(tweets) >= 10:
                self.disconnect()

    def on_error(self, status_code, data):
        self.disconnect


stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
stream.statuses.filter(track='weather freezing,weather black ice,weather hot,weather ice,weather blizzard,weather blustery,weather breeze,weather calm,weather cloud,weather cloudy,weather cold,weather cold front,weather downpour,weather drizzle,weather fair,weather flash flood,weather flood,weather flurry,weather fog,weather fog bank,weather freeze,weather freezing rain,weather frost,weather gale,weather ground fog,weather gust,weather hail,weather heat,weather heat wave,weather humid,weather humidity,weather ice,weather ice age,weather ice crystals,weather ice pellets,weather ice storm,weather icicle,weather mist,weather moisture,weather overcast,weather partly cloudy,weather permafrost,weather polar,weather polar front,weather precipitation,weather pressure,weather prevailing wind,weather radar,weather rain,weather rainbands,weather rainbow,weather rain gauge,weather sky,weather sleet,weather slush,weather snow,weather snowfall,weather snowflake,weather snow,weather flurry,weather snow level,weather snow line,weather snow shower,weather snowstorm,weather spring,weather steam,weather storm,weather storm surge,weather storm tracks,weather summer,weather sunrise,weather sunset,weather temperature,weather thaw,weather thermal,weather thunder,weather thunderstorm,weather tropical depression,weather tropical disturbance,weather tropical storm,weather tropical wave,weather typhoon,weather visibility,weather vortex,weather warm,weather water,weather water cycle,weather weather,weather weathering,weather whirlwind,weather whiteout,weather wind,weather wind chill,weather wind chill factor,weather wind shear,weather blizzard,weather blustery,weather breeze,weather calm,weather cloud,weather cloudy,weather cold,weather cold front,weather downpour,weather drizzle,weather fair,weather flash flood,weather flood,weather flurry,weather fog,weather fog bank,weather freeze,weather freezing rain,weather frost,weather gale,weather ground fog,weather gust,weather hail,weather heat,weather heat wave,weather humid,weather humidity,weather ice,weather ice age,weather ice crystals,weather ice pellets,weather ice storm,weather icicle,weather mist,weather moisture,weather overcast,weather partly cloudy,weather permafrost,weather polar,weather polar front,weather precipitation,weather pressure,weather prevailing wind,weather radar,weather rain,weather rainy,weather raining,weather rainbow,weather sky,weather sleet,weather slush,weather snow,weather snow,weather flurry,weather snow level,weather snow line,weather snow shower,weather snowstorm,weather spring,weather steam,weather storm,weather storm surge,weather storm tracks,weather summer,weather sun,weather sunny,weather sunrise,weather sunset,weather temperature,weather thaw,weather thermal,weather thunder,weather thunderstorm,weather tropical depression,weather tropical disturbance,weather tropical storm,weather tropical wave,weather typhoon,weather visibility,weather vortex,weather warm,weather water,weather water cycle,weather weather,weather weathering,weather whirlwind,weather whiteout,weather wind,weather wind chill,weather wind chill factor,weather wind shear')

with open(r"c:\data\twitter_scrape_pickle", "wb") as p:
    pickle.dump(tweets, p)

with open(r'c:\\data\\twitter_scrape_pickle', 'rb') as p1:
    tweets = pickle.load(p1)
    frame = DataFrame(tweets)
    frame2 = frame['text']
# frame2.to_csv("c:\\data\\twitter_scrape" + cur_time_stamp + ".csv", sep=',', encoding='utf-8')
frame2.to_csv("c:\\data\\test1312.csv", sep=',', encoding='utf-8')
# with open(r"c:\data\twitter_scrape.csv", "w") as tw:
#     for t in tweets:
#         text2 = t['text'].encode('utf-8')
#         create2 = t['created_at']
#         tw.write(text2 + '|' + create2)






