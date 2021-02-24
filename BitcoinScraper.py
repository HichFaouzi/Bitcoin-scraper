from bs4 import BeautifulSoup
import pandas as pd
import requests
from IPython.display import display
from time import time, sleep
from pymongo import MongoClient 
from itertools import chain

def scraper():
    Hashes2 = []
    Values2 = []

    df = pd.DataFrame(columns=['hash', 'time', 'BTC Value','USD Value'])
    col = ['hash', 'time', 'BTC Value','USD Value']
    url = "https://www.blockchain.com/btc/unconfirmed-transactions"
    html_page = requests.get(url)
    soup = BeautifulSoup(html_page.content,'html.parser')

    Hashes = soup.findAll("a", {"class": "sc-1r996ns-0 fLwyDF sc-1tbyx6t-1 kCGMTY iklhnl-0 eEewhk d53qjk-0 ctEFcK"})
    Values = soup.findAll("span", {"class": "sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC"})

    for i in Values:
        Values2.append(i.text)
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


    df = pd.DataFrame(data = FinalList,columns = col)
    df.sort_values(by=['BTC Value'], inplace=True, ascending=False)
    df_list = df.iloc[:1].values.tolist()
    flatten_list = list(chain.from_iterable(df_list))
    conn = MongoClient()
    db = conn["BTCscraper_db"]
    mydict = { "Hash": flatten_list[0], "Time": flatten_list[1], "BTC_Value": flatten_list[2], "USD": flatten_list[3] }
    db.BTC_Collection.insert_one(mydict)
    print(df.iloc[:1])

while True:
    scraper()
    sleep(60 - time() % 60)

