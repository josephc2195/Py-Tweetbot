import tweepy

class TwitterBot:

    def __init__(self, credentials):
        self.auth = tweepy.OAuthHandler(credentials["CONSUMER_KEY"], credentials["CONSUMER_SECRET"])
        self.auth.set_access_token(credentials["ACCESS_TOKEN"], credentials["ACCESS_TOKEN_SECRET"])
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True)

    def tweet(self, tweet):
        self.api.update_status(tweet)

    def friend(self, user):
        self.api.create_friendship(user)
