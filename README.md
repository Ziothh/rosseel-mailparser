# Agence Rosseel mailparser
Deze mailparser heb ik gemaakt voor [Agence Rosseel](https://www.rosseel.be).

De parser wordt gerunned door een Cronjob. Dan zal het alle emails met leads verwerken en doorsturen naar de API van Rosseel.

Er zit al heel wat basis functionaliteit in en het is geschreven op een manier die makkelijk nieuwe uitbreidingen toelaat zonder dat een groot stuk code herwerkt moet worden.

Post Scriptum: Sommige data zoals paswoorden, enz. zijn om vanzelfsprekende redenen verwijderd.

## Functionaliteit
De mailparser zal:
 - een mail verwerken en de gevraagde data uit de html halen
 - deze data bewerken (indien nodig) en doorsturen naar een webhook

## Toekomstige Features
 - Mogenlijkheid om excel bestanden, die meegegeven worden in mails, te verwerken
 - Webscraping voor gewenste data die niet in de mail body werd meegegeven maar wel online te zien is.
 - Script om nieuwe mail content types snel te registreren in plaats van dit manueel in json data te schrijven 


## Gebruikte Libraries
 - [beautifulsoup4](https://pypi.org/project/beautifulsoup4): html parsing
 - [lxml](https://pypi.org/project/lxml): in samenwerking met beautifulsoup4
 - [pandas](https://pypi.org/project/pandas): excel parsing (zie: toekomstige feature)
 - [regex](https://pypi.org/project/regex)
 - [requests](https://pypi.org/project/requests): communicatie met de Rosseel API
