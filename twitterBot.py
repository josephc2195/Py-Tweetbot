import tweepy
import pandas 

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
        #self.api.search(q=keywords, lang="en", rpp=10)
        for wrd in self.api.search(q=keywords, lang="en", rpp=10):
            print(f"{wrd.user.name}:{wrd.text}")
            print("")
    
    def follow(self):
        for follower in tweepy.Cursor(self.api.followers).items():
            follower.follow()
            print(f"Followed user @{follower.screen_name}")
        print("Finished following everyone in your followers list!")

    def dm(self, name, body):
        id = self.api.get_user(name).id_str
        self.api.send_direct_message(id, body)
        print(f"Message sent to {name}: {body}")

    def global_trends(self):
        print("Top 10 trending topics in the world: ")
        for t in self.api.trends_place(1)[0]["trends"][:10]:
            print(t["name"])

    def trends(self, place):
        print(f"Top 10 trending topics in {place}: ")
        if place == "New York" or place == "NY":
            for t in self.api.trends_place(2459115)[0]["trends"][:10]:
                print(t["name"])
        elif place == "Los Angeles" or place == "LA":
            for t in self.api.trends_place(2442047)[0]["trends"][:10]:
                print(t["name"])
        elif place == "London":
            for t in self.api.trends_place(44418)[0]["trends"][:10]:
                print(t["name"])
        elif place == "Chicago":
            for t in self.api.trends_place(2379574)[0]["trends"][:10]:
                print(t["name"])
        elif place == "USA" or place == "US":
            for t in self.api.trends_place(23424977)[0]["trends"][:10]:
                print(t["name"])
        elif place == "Japan":
            for t in self.api.trends_place(23424856)[0]["trends"][:10]:
                print(t["name"])
            
            