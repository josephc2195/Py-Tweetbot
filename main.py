import sys
import config
from twitterBot import TwitterBot


bot = TwitterBot(config.credentials)

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