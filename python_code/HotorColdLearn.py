from pandas import DataFrame
import pandas as pd
import csv
import nltk


with open(r"C:\data\twitter_scrapedatamining1.csv", "r") as t:
    treader = csv.reader(t)
    twlist = []
    for i in treader:
        twlist.append(i)
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

word_features = get_word_features(get_words_in_tweets(twtokens))


def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

training_set = nltk.classify.apply_features(extract_features, twtokens)
classifier = nltk.NaiveBayesClassifier.train(training_set)
# print classifier.show_most_informative_features(32)
tweet = 'sunny park pressure'
print classifier.classify(extract_features(tweet.split()))
# print classifier.classify(extract_features(tweet.split()))
