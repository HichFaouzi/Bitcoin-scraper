# Bitcoin-scraper

Met de scraper die ik heb gemaakt kan je krijg je elk minuut de bitcoinhash met de grootste waarde te zien. Hieronder geef ik een opsomming van instructies om de code te kunnen gebruiken op een linux PC.

Open de terminal en kopieer de repository:
###### git clone https://github.com/HichFaouzi/Bitcoin-scraper.git

Navigeer naar de map die je net hebt gedownload en installeer de requirements.txt file:
###### pip install -r requirements.txt

Vervolgens is alles klaar om de scraper te runnen. De code zal de Hash met hoogste waarde afdrukken en over ongeveer een minuut (afhankelijk van runtime) wordt de volgende hoogste hash met waarde getoond. Run volgende code. Afhankelijk van welke python versie je gebruikt zal je een van de 2 lijnen moeten proberen

Python:
###### python BitcoinScraper.py

Python3:
###### python3 BitcoinScraper.py
