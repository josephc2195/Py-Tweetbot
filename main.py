import sys
from tweepBot import TwitterBot

credentials = {
    "CONSUMER_KEY": "EDuAwY6n75xAMqN1de4m3ba6o",
    "CONSUMER_SECRET": "TPhQviO91fank70pdFx0QLhpwWhK8fCrdC0zOIgV1PGhG11gHF",
    "ACCESS_TOKEN": "1241156834959994884-dXg2FkueZOfwZMurobWi0lNYEYcaR5",
    "ACCESS_TOKEN_SECRET": "KHXdQtvffkZy7EQISubP1570NFBrS5qC6vQKpVnkctvVO"
}

bot = TwitterBot(credentials)

if sys.argv[1] == "tweet":
    bot.tweet(sys.argv[2])

if sys.argv[1] == "friend":
    bot.friend(sys.argv[2])
