# Bitcoin-scraper

Met de scraper die ik heb gemaakt krijg je elk minuut de bitcoinhash met de grootste waarde te zien.Deze worden ook automatisch weggeschreven in en mongodb database. Vooraleer de data wordt doorgeschreven naar mongodb wordt deze tijdelijk opgeslagen in een Redis Caching databank. Hieronder geef ik een opsomming van instructies om het project te kunnen installeren en runnen op een Linux Computer.

Open de terminal en kopieer de repository:
##### git clone https://github.com/HichFaouzi/Bitcoin-scraper.git

Navigeer naar de map die je net hebt gedownload en installeer de requirements.txt file:
###### pip install -r requirements.txt
Het kan zijn dat je eerst nog pip moet installeren voor je OS.
###### sudo apt install pip

Nu gaan we mongodb installeren en opzetten. Dit gebeurt automatisch door het bash scriptje 'install_mongodb" te runnen. voer volgende commando's uit:
eerst toegang geven tot het script:
###### chmod +x /<Path_to_directory>/install_mongodb.sh
Navigeer naar de map en voer volgend commando uit:
###### ./install_mongodb.sh

Nu gaan we de Redis Caching databank installeren en opzetten. Dit doen we door het bash scriptje "install_redis" te runnen. Voor volgende commando's uit:
eerst toegang geven tot het script:
###### chmod +x /<Path_to_directory>/install_redis.sh
Navigeer naar de map en voer volgend commando uit:
###### ./install_redis.sh

Vervolgens is alles klaar om de scraper te runnen. De scraper is opgedeeld in 2 scripts. Het eerste script zal data scrapen en opslaan in Redis. Deze data zal na 60 seconden verwijderd worden. Om het script te stoppen houd dan de toetsen CTRL + C ingedrukt en run het 2de scriptje. Het 2de scriptje zal de data extracten uit redis en daarvan de Hash met de hoogste waarde opslaan in mongodb. De gebruiker moet de scriptjes zelf stoppen met runnen. LET OP: Als je een minuut wacht met het runnen van het 2de scriptje dan zal er geen data worden weggeschreven naar mongodb omdat de redis databank al leeg gemaakt is. 

Eerste scrip runnen:
##### python3 BitcoinScraper.py


Tweede script runnen:
##### python3 ExtractAndToMongoDb.py

Om het script te laten stoppen druk op volgende toetsen: CTRL + C


Om de databank te zien voer volgende commando's uit:

##### systemctl start mongod
##### mongo
##### use BTCscraper_db
##### db.BTC_Collection.find()
