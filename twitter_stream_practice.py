from twython import TwythonStreamer


tweets = []
CONSUMER_KEY = 'Cm099MoBTeVX1j1ZXsi0c2hZP'
CONSUMER_SECRET = 'Uqmb4xnVjnMw9h05HzHKxXcTdpNa3aH0cy9AIaJseIgmLDN9Fa'
ACCESS_TOKEN = '803229807504986114-0woyC72IkNnUWN7KJxnqYSp4WI4pdq7'
ACCESS_TOKEN_SECRET = 'eC1EJRIZClscMoVMXb8xIx9t0OgiwyNozNsqewlsFt9r2'


class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if data['lang'] == 'en':
            tweets.append(data)
            print 'received tweet no', len(tweets)

        if len(tweets) >= 10:
            self.disconnect()

    def on_error(self, status_code, data):
        self.disconnect


stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
stream.statuses.filter(track='clash')

with open(r"c:\data\twitter_scrape.json", "w") as tw:
    for t in tweets:
        tw.write(str(t))


