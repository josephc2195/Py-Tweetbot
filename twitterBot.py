import tweepy

class TwitterBot:

    #this is used to authenticate the credentials 
    def __init__(self, credentials):
        self.auth = tweepy.OAuthHandler(credentials["CONSUMER_KEY"], credentials["CONSUMER_SECRET"])
        self.auth.set_access_token(credentials["ACCESS_TOKEN"], credentials["ACCESS_TOKEN_SECRET"])
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True)

    def tweet(self, tweet):
        self.api.update_status(tweet)
        print(f"New Tweet from user: {tweet}")

    def friend(self, user):
        self.api.create_friendship(user)

    def search(self, keywords):
        self.api.search(q=keywords, lang="en", rpp=10)
        for wrd in self.api.search(q=keywords, lang="en", rpp=10):
            print(f"{wrd.user.name}:{wrd.text}")
            print("")
    
    def follow(self):
        count = 0
        for follower in tweepy.Cursor(self.api.followers).items():
            follower.follow()
            count+= 1
            if count == 7:
                print(f"Now following @{follower}")
            
            