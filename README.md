# Bitcoin-scraper

Met de scraper die ik heb gemaakt krijg je elk minuut de bitcoinhash met de grootste waarde te zien.Deze worden ook automatisch weggeschreven in en mongodb database. Hieronder geef ik een opsomming van instructies om de code te kunnen gebruiken op een linux PC.

Open de terminal en kopieer de repository:
###### git clone https://github.com/HichFaouzi/Bitcoin-scraper.git

Navigeer naar de map die je net hebt gedownload en installeer de requirements.txt file:
###### pip install -r requirements.txt
Het kan zijn dat je eerst nog pip moet installeren voor je OS.
###### sudo apt install pip

Nu gaan we mongodb installeren en opzetten. Dit gebeurt automatisch door het bash scriptje 'install_mongodb" te runnen. voer volgende commando's uit:
eerst toegang geven tot het script:
###### chmod +x /path/to/yourscript.sh
nu het scriptje runnen:
###### /path/to/yourscript.sh
als je al in de directory zit waar het script in zit voer dan volgend commando uit:
###### ./yourscript.sh
Vervolgens is alles klaar om de scraper te runnen. De code zal de Hash met hoogste waarde afdrukken en over ongeveer een minuut (afhankelijk van runtime) wordt de volgende hash met hoogste waarde van op dat moment getoond. Ook zullen de lijnen die getoond worden ook worden weggeschreven in een mongodb databank. Run volgende code. Afhankelijk van welke python versie je gebruikt zal je een van de 2 lijnen moeten proberen

Python3:
#### python3 BitcoinScraper.py

Om het script te laten stoppen druk op volgende toetsen: CTRL + C

Om de databank te zien voer volgende commando's uit:

##### systemctl start mongod
##### mongo
##### use BTCscraper_db
##### db.BTC_Collection.find()
