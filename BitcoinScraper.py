from bs4 import BeautifulSoup
import pandas as pd
import requests
from IPython.display import display
from time import time, sleep
from pymongo import MongoClient
from itertools import chain
import redis
client = MongoClient()
rdis = redis.Redis(host='localhost', port=6379)

def scraper():
    Hashes2 = []
    url = "https://www.blockchain.com/btc/unconfirmed-transactions"
    html_page = requests.get(url)
    soup = BeautifulSoup(html_page.content,'html.parser')

    Hashes = soup.findAll("a", {"class": "sc-1r996ns-0 fLwyDF sc-1tbyx6t-1 kCGMTY iklhnl-0 eEewhk d53qjk-0 ctEFcK"})
    Values = soup.findAll("span", {"class": "sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC"})
    Values2 = [i.contents[0].replace('$', '').replace(',', '') for i in Values]
    for i in Hashes:
        Hashes2.append(i.text)
    def chunks(l, n):
        # For item i in a range that is a length of l,
        for i in range(0, len(l), n):
            # Create an index range for l of n items:
            yield l[i:i+n]
    FinalList = list(chunks(Values2, 3))

    for i in range(0,len(Hashes2)):
        FinalList[i].insert(0,Hashes2[i])

    hasharr = [i[0] for i in FinalList]
    timearr = [i[1] for i in FinalList]
    btcarr = [i[2] for i in FinalList]
    usdarr = [i[3] for i in FinalList]
    for i in hasharr:
        rdis.rpush("Hash", i)
    for i in timearr:
        rdis.rpush("Time", i)
    for i in btcarr:
        rdis.rpush("BTC-Value", i)
    for i in usdarr:
        rdis.rpush("USD-Value", i)
    rdis.expire("Hash", 60)
    rdis.expire("Time", 60)
    rdis.expire("BTC-Value", 60)
    rdis.expire("USD-Value", 60)

while True:
    scraper()
    sleep(60 - time() % 60)
