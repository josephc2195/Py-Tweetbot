import tweepy

class TwitterBot:

    def __init__(self, credentials):
        self.auth = tweepy.OAuthHandler(credentials("CONSUMER_KEY"), credentials("CONSUMER_SECRET"))
        self.auth.set_access_token(credentials("ACCESS_TOKEN"), credentials("ACCESS_TOKEN_SECRET"))
        self.api = tweepy.API(self.auth, wait_on_rate_limit:True)

    def tweet(self, tweet):
        self.api.update_status(tweet)

    def friend(self, user):
        self.api.create_friendship(user)


#personal keys
CONSUMER_KEY = "EDuAwY6n75xAMqN1de4m3ba6o"
CONSUMER_SECRET = "TPhQviO91fank70pdFx0QLhpwWhK8fCrdC0zOIgV1PGhG11gHF"
ACCESS_TOKEN = "1241156834959994884-dXg2FkueZOfwZMurobWi0lNYEYcaR5"
ACCESS_TOKEN_SECRET = "KHXdQtvffkZy7EQISubP1570NFBrS5qC6vQKpVnkctvVO"

#Authenticating to twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

#api object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

#send a tweet:
api.update_status("Milo is the guy")

#user
user = api.get_user("mr_jnc")
name = user.name
description = user.description
location = user.location
print(f"{name}, is from {location}. They are {description}")
print(user)

#start following a user
api.create_friendship("mr_jnc")

#shows timelines of selected user
tl = api.home_timeline()
#for tweet in tl:
#    print(f"{tweet.user.name} said {tweet.text}")

#update user profile
#api.update_profile(description="changes made from python")
print("trends: ")
trends_result = api.trends_place(1)
for trend in trends_result[0]["trends"]:
    print(trend["name"])
