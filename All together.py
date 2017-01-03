from pandas import DataFrame
import pandas as pd
import csv
import nltk
from twython import TwythonStreamer
import pickle
from pandas import DataFrame, Series
import datetime
# Machine learning for weather or not weather
with open(r"C:\data\weatherlearning.csv", "r") as w:
    wreader = csv.reader(w)
    wwlist = []
    for i in wreader:
        wwlist.append(i)
wwtokens = []

for (words, sentiment) in wwlist:
    wwords_filtered = [e.lower() for e in str(words).split() if len(e) >= 3]
    wwtokens.append((wwords_filtered, sentiment))


def get_words_in_tweets(tweets):
    wall_words = []
    for (words, sentiment) in tweets:
        wall_words.extend(words)
    return wall_words


def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

word_features = get_word_features(get_words_in_tweets(wwtokens))


def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

training_setw = nltk.classify.apply_features(extract_features, wwtokens)
classifierw = nltk.NaiveBayesClassifier.train(training_setw)
# Machine learning for positive or neagtive
with open(r"C:\data\positive_or_negative.csv", "r") as w:
    preader = csv.reader(w)
    pwlist = []
    for i in preader:
        pwlist.append(i)
pwtokens = []

for (words, sentiment) in pwlist:
    pwords_filtered = [e.lower() for e in str(words).split() if len(e) >= 3]
    pwtokens.append((pwords_filtered, sentiment))


def get_words_in_tweets(tweets):
    pall_words = []
    for (words, sentiment) in tweets:
        pall_words.extend(words)
    return pall_words


def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

pword_features = get_word_features(get_words_in_tweets(pwtokens))


def extract_features(document):
    document_words = set(document)
    pfeatures = {}
    for word in pword_features:
        pfeatures['contains(%s)' % word] = (word in document_words)
    return pfeatures

training_setp = nltk.classify.apply_features(extract_features, pwtokens)
classifierp = nltk.NaiveBayesClassifier.train(training_setp)
# Machine learning for hot or cold
with open(r"C:\data\hot_or_cold_learning.csv", "r") as t:
    treader = csv.reader(t)
    twlist = []
    for j in treader:
        twlist.append(j)
twtokens = []

for (words, sentiment) in twlist:
    words_filtered = [e.lower() for e in str(words).split() if len(e) >= 3]
    twtokens.append((words_filtered, sentiment))


def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
        all_words.extend(words)
    return all_words


def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

hword_features = get_word_features(get_words_in_tweets(twtokens))


def extract_features(document):
    document_words = set(document)
    hfeatures = {}
    for word in hword_features:
        hfeatures['contains(%s)' % word] = (word in document_words)
    return hfeatures

training_seth = nltk.classify.apply_features(extract_features, twtokens)
classifierh = nltk.NaiveBayesClassifier.train(training_seth)
# classifier set up now start twitter import
tweets = []
CONSUMER_KEY = 'INSERT KEY'
CONSUMER_SECRET = 'INSERT KEY'
ACCESS_TOKEN = 'INSERT KEY'
ACCESS_TOKEN_SECRET = 'INSERT KEY'

cur_time_stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H")


class MyStreamer(TwythonStreamer):

    def on_success(self, data):
            tweets.append(data)
            print len(tweets)

            if len(tweets) >= 1000:
                self.disconnect()

    def on_error(self, status_code, data):
        self.disconnect


stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
stream.statuses.filter(track='weather freezing,weather black ice,weather hot,weather ice,weather blizzard,weather blustery,weather breeze,weather calm,weather cloud,weather cloudy,weather cold,weather cold front,weather downpour,weather drizzle,weather fair,weather flash flood,weather flood,weather flurry,weather fog,weather fog bank,weather freeze,weather freezing rain,weather frost,weather gale,weather ground fog,weather gust,weather hail,weather heat,weather heat wave,weather humid,weather humidity,weather ice,weather ice age,weather ice crystals,weather ice pellets,weather ice storm,weather icicle,weather mist,weather moisture,weather overcast,weather partly cloudy,weather permafrost,weather polar,weather polar front,weather precipitation,weather pressure,weather prevailing wind,weather radar,weather rain,weather rainbands,weather rainbow,weather rain gauge,weather sky,weather sleet,weather slush,weather snow,weather snowfall,weather snowflake,weather snow,weather flurry,weather snow level,weather snow line,weather snow shower,weather snowstorm,weather spring,weather steam,weather storm,weather storm surge,weather storm tracks,weather summer,weather sunrise,weather sunset,weather temperature,weather thaw,weather thermal,weather thunder,weather thunderstorm,weather tropical depression,weather tropical disturbance,weather tropical storm,weather tropical wave,weather typhoon,weather visibility,weather vortex,weather warm,weather water,weather water cycle,weather weather,weather weathering,weather whirlwind,weather whiteout,weather wind,weather wind chill,weather wind chill factor,weather wind shear,weather blizzard,weather blustery,weather breeze,weather calm,weather cloud,weather cloudy,weather cold,weather cold front,weather downpour,weather drizzle,weather fair,weather flash flood,weather flood,weather flurry,weather fog,weather fog bank,weather freeze,weather freezing rain,weather frost,weather gale,weather ground fog,weather gust,weather hail,weather heat,weather heat wave,weather humid,weather humidity,weather ice,weather ice age,weather ice crystals,weather ice pellets,weather ice storm,weather icicle,weather mist,weather moisture,weather overcast,weather partly cloudy,weather permafrost,weather polar,weather polar front,weather precipitation,weather pressure,weather prevailing wind,weather radar,weather rain,weather rainy,weather raining,weather rainbow,weather sky,weather sleet,weather slush,weather snow,weather snow,weather flurry,weather snow level,weather snow line,weather snow shower,weather snowstorm,weather spring,weather steam,weather storm,weather storm surge,weather storm tracks,weather summer,weather sun,weather sunny,weather sunrise,weather sunset,weather temperature,weather thaw,weather thermal,weather thunder,weather thunderstorm,weather tropical depression,weather tropical disturbance,weather tropical storm,weather tropical wave,weather typhoon,weather visibility,weather vortex,weather warm,weather water,weather water cycle,weather weather,weather weathering,weather whirlwind,weather whiteout,weather wind,weather wind chill,weather wind chill factor,weather wind shear')
 # writing tweets to pickle
with open(r"c:\data\twitter_scrape_pickle", "wb") as p:
     pickle.dump(tweets, p)

# taking tweets from pickle and putting them into csv
with open(r'c:\\data\\twitter_scrape_pickle', 'rb') as p1:
    tweets = pickle.load(p1)
    frame = DataFrame(tweets)
    frame2 = frame['text'].replace('\n', ' ')
frame2.to_csv("c:\\data\\test1312.csv", sep=',', encoding='utf-8')
# adding classification to csv
with open("c:\\data\\test1312.csv", "r") as csvinput:
    with open("c:\\data\\test1319.csv", "w") as csvoutput:
        writer = csv.writer(csvoutput)
        for row in csv.reader(csvinput):
            writer.writerow([row[1]] + [classifierw.classify(extract_features(str(row[1]).split()))] + [classifierh.classify(extract_features(str(row[1]).split()))] + [classifierp.classify(extract_features(str(row[1]).split()))] + ['03/01/2017'])



