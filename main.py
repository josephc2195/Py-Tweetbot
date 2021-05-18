import sys
from twitterBot import TwitterBot

credentials = {
    "CONSUMER_KEY": "ExHzjjl1dSjff4rNMDMEaVSRk",
    "CONSUMER_SECRET": "CqzcyIJXfkoZtfol8qXgcLCDQ7BKjqCCAKX7iWiA3FFwTMfzpi",
    "ACCESS_TOKEN": "1241156834959994884-YH7zjfDITY95N5a0Q5FE2a40Ylf6lO",
    "ACCESS_TOKEN_SECRET": "vy4NjMY4KTwyJxtlyuYwFttRFdqv2DbxPd28fPhNsVa3D"
}

bot = TwitterBot(credentials)

if sys.argv[1] == "tweet":
    bot.tweet(sys.argv[2])

if sys.argv[1] == "friend":
    bot.friend(sys.argv[2])

if sys.argv[1] == "search":
    bot.search(sys.argv[2])

if sys.argv[1] == "follow":
    bot.follow()

if sys.argv[1] == "dm":
    bot.dm(sys.argv[2], sys.argv[3])

if sys.argv[1] == "trends":
    if len(sys.argv) < 3: 
        bot.global_trends()
    else:
        bot.trends(sys.argv[2])