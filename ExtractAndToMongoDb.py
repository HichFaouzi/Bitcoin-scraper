from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
from pymongo import MongoClient
import redis

client = MongoClient()
rdis = redis.Redis(decode_responses=True)
db = client["BTCscraper_db"]
def ExtractAndToMongo():
    hashes = list(map(str, rdis.lrange("Hash", 0, -1)))
    times = list(map(str, rdis.lrange("Time", 0, -1)))
    btc = list(map(str, rdis.lrange("BTC-Value", 0, -1)))
    usd = list(map(float, rdis.lrange("USD-Value", 0, -1)))
    i = usd.index(max(usd))
    highestHash = hashes[i]
    highestTime = times[i]
    highestBtc = btc[i]
    mydict = { "Hash": highestHash, "Time": highestTime, "BTC_Value": highestBtc, "USD": max(usd) }
    db.BTC_Collection.insert_one(mydict)

while True:
    ExtractAndToMongo()
    time.sleep(60)