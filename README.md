# Agence Rosseel mailparser
Deze mailparser heb ik gemaakt voor Agence Rosseel.

Er zit al heel wat basis functionaliteit in en ik heb de parser geschreven op een manier die makkelijk nieuwe uitbreidingen toelaat zonder dat een groot stuk code herwerkt moet worden.

Post Scriptum: Sommige data zoals paswoorden, enz. zijn om vanzelfsprekende redenen verwijderd.

## Functionaliteit
De mailparser zal:
 - een mail verwerken en de gevraagde data uit de html halen
 - deze data bewerken (indien nodig) en doorsturen naar een webhook

## Toekomstige Features
 - Mogenlijkheid om excel bestanden, die meegegeven worden in mails, te verwerken
 - Webscraping voor gewenste data die niet in de mail body werd meegegeven maar wel online te zien is.
 - Script om nieuwe mail content types snel te registreren in plaats van dit manueel in json data te schrijven 