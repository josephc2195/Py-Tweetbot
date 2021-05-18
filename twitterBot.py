import tweepy
import pandas 
from datetime import datetime

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
        toTxt = f"Trending topics in the world on {datetime.now()} \n"
        for t in self.api.trends_place(1)[0]["trends"][:10]:
            print(t["name"])
            toTxt += t["name"] + "\n"
        f = open("world_trends.txt", "a", encoding="utf-8") 
        f.write(toTxt)
        f.close()
        f = open("world_trends.txt", "r")
        print(f.read())

    def trends(self, place):
        print(f"Top 10 trending topics in {place}: ")
        toTxt = f"Trending topics in {place} on {datetime.now()} \n"
        if place == "New York" or place == "NY":
            for t in self.api.trends_place(2459115)[0]["trends"][:10]:
                print(t["name"])
                toTxt += t["name"] + "\n"
        elif place == "Los Angeles" or place == "LA":
            for t in self.api.trends_place(2442047)[0]["trends"][:10]:
                print(t["name"])
                toTxt += t["name"] + "\n"
        elif place == "San Diego" or place == "SD":
            for t in self.api.trends_place(2487889)[0]["trends"][:10]:
                print(t["name"]) 
                toTxt += t["name"] + "\n"
        elif place == "London":
            for t in self.api.trends_place(44418)[0]["trends"][:10]:
                print(t["name"])
                toTxt += t["name"] + "\n"
        elif place == "Chicago":
            for t in self.api.trends_place(2379574)[0]["trends"][:10]:
                print(t["name"])
                toTxt += t["name"] + "\n"
        elif place == "USA" or place == "US":
            for t in self.api.trends_place(23424977)[0]["trends"][:10]:
                print(t["name"])
                toTxt += t["name"] + "\n"
        elif place == "Japan":
            for t in self.api.trends_place(23424856)[0]["trends"][:10]:
                print(t["name"])
                toTxt += t["name"] + "\n"
        f = open(f"{place}_trends.txt", "a", encoding="utf-8") 
        f.write(toTxt)
        f.close()
        f = open(f"{place}_trends.txt", "r")
        print(f.read())
        
            
            