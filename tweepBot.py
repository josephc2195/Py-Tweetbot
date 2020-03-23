import tweepy

#personal keys
CONSUMER_KEY = 'EDuAwY6n75xAMqN1de4m3ba6o'
CONSUMER_SECRET = 'TPhQviO91fank70pdFx0QLhpwWhK8fCrdC0zOIgV1PGhG11gHF'
ACCESS_TOKEN = '1241156834959994884-dXg2FkueZOfwZMurobWi0lNYEYcaR5'
ACCESS_TOKEN_SECRET = 'KHXdQtvffkZy7EQISubP1570NFBrS5qC6vQKpVnkctvVO'

#Authenticating to twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)


#send a tweet:
#api.update_status("tweeting with python")

#user
user = api.get_user("mr_jnc")
name = user.name
description = user.description
location = user.location


#start following a user
#api.create_friendship("mr_jnc")

#shows timelines of selected user
tl = api.home_timeline()
#for tweet in tl:
#    print(f"{tweet.user.name} said {tweet.text}")
