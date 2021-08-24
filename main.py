import discord
import os
import ninekbot
import pymongo
import requests

from dotenv import load_dotenv
load_dotenv()

token = os.getenv("DISCORD_TOKEN")

mongodbUser = str(os.getenv("MONGODB_USER"))
mongodbPass = str(os.getenv("MONGODB_PASS"))
mongoClient = pymongo.MongoClient("mongodb+srv://"+mongodbUser+":"+mongodbPass+"@cluster0.zkv55.mongodb.net/Allin_DB.nephest?retryWrites=true&w=majority")
collection = mongoClient['Allin_DB']['nephest']


client = discord.Client()
bot = ninekbot.Ninekbot(token, client, mongoClient, collection)

print(discord.__version__)
print(pymongo.__version__)
print(requests.__version__)

#bot.startup()