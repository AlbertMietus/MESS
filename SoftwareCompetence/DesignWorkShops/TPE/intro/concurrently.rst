.. Copyright (C) 2017-2019: ALbert Mietus.


Why concurrently?
=================

Vaak is het wenselijk om (a) veel *soortgelijke taken tegelijkertijd* uit te voeren. Dit (b) op de
*achtergrond* te doen; zodat het 'hoofdprogramma' beschikbaar blijft, bijvoorbeeld voor
interactie. En (c), dit werk te verdelen meerdere processors; om zo de doorlooptijd te verkorten.

Deze *concurrency* kan met diverse primitieven gerealiseerd worden. Bijvoorbeeld met meerdere
computer-nodes, met meerdere processen, of met meerdere *threads*. De juiste keuze is sterk
afhankelijk van de relative (communicatie) overhead: hoe kleiner de taak, hoe minder overhead
toegestaan is. Daarom zijn threads populair. Maar ook het opstarten van een thread kost tijd; te
veel tijd voor de kleinste, repeterende taken. Het :dfn:`WorkersPool` patroon is een geavanceerde,
generieke aanpak, die de minste overhead kent. Zeker als deze geïmplementeerd word met threads. Dan
mag de taak zo klein zijn als *één functie*!

Al zijn er ook vele andere redenen om een ‘WorkersPool’ te gebruiken. Zoals:

Robuustheid
-----------

Door werk te verdelen over meerdere processen, of nodes, is een zekere *'redundancy'* ingebouwd. Met behulp van een ‘broker’ kunnen mislukte (gecrashde) taken vaak opnieuw opgestart worden.

Schaalbaar
----------

Door (steeds) meer *werkers* in te zetten is de oplossing erg schaalbaar. Een bekend voorbeeld hiervan is de (apache) webserver. Deze maakt gebruik van het WorkersPool principe op meerdere niveaus. Zowel met threads & processen op één systeem, en middels ‘load-balancers' tussen systemen en “in de cloud”.

Eenvoudig
---------

Hoewel de (thread) WorkersPool complex is om te implementeren, maakt een goede realisatie (lees: interface) het gebruik van concurrency eenvoudig. Een goed voorbeeld hiervan is `Grand Central Dispatch <https://en.wikipedia.org/wiki/Grand_Central_Dispatch>`__ van Apple. Deze technology is o.a. gebaseerd op de WorkersPool en goed geïntegreerd; waardoor vele (zelfs beginende) programmeurs dit principe (onbewust) gebruiken.

*GCD* is ook bekend als :dfn:`libdispatch` en beschikbaar voor o.a.
`FreeBSD  <https://wiki.freebsd.org/GCD>`__,
`Linux <http://nickhutchinson.me/libdispatch>`__ en onderdeel van de (open-source)
`Swift-Libraries  <https://apple.github.io/swift-corelibs-libdispatch/>`__.


