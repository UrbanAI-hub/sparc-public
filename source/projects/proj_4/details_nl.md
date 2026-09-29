### Overzicht
Wat maakt een buurt aantrekkelijk? Door meer dan 200.000 straatbeelden te analyseren met geavanceerde computer vision, onthult dit project de verborgen visuele factoren — zoals bladerdak en fietsactiviteit — die de huizenprijzen in Rotterdam bepalen. De bevindingen bieden een nieuwe kijk op hoe het straatbeeld direct van invloed is op de vastgoedwaarde.

### De uitdaging
Traditionele vastgoedmodellen leunen zwaar op structurele basiskenmerken: woonoppervlakte, bouwjaar en het aantal kamers. Toch weet iedereen die een huis zoekt, dat de sfeer van een straat net zo belangrijk is. Deze standaardtaxaties missen vaak de bredere omgevingscontext, van de rust van nabijgelegen parken tot het lawaai van een drukke snelweg. Daardoor kunnen twee identieke huizen op papier dezelfde prijs hebben, zelfs als de ene aan een levendige, lommerrijke laan ligt en de andere aan een grijze, betonnen verkeersader. Deze blinde vlek leidt tot onnauwkeurige vastgoedwaarderingen en negeert de economische waarde van goed ontworpen openbare ruimtes.

### Doelstellingen
- **Kwantificeren** hoe visuele stedelijke kenmerken — zoals groen, voetgangers, auto's en fietsen — die uit straatbeelden worden gehaald, de huizenprijzen in Rotterdam beïnvloeden.
- **Vergelijken** van de voorspellende kracht van traditionele lineaire waarderingsmodellen met flexibele machine learning-benaderingen.
- **In kaart brengen** van de ruimtelijke voetafdruk van straatbeeldelementen om te begrijpen hoe hun economische impact verandert naarmate de afstand tot een woning toeneemt.

### Aanpak
Het onderzoeksteam koppelde 6.691 woningadvertenties in Rotterdam aan een enorme dataset van meer dan 200.000 Google Street View-beelden. Ze gebruikten semantische segmentatie — een computer vision-techniek die werkt als een digitale markeerstift — om de exacte hoeveelheid zichtbaar groen in een straat te meten. Daarnaast telden objectdetectiemodellen dynamische elementen zoals mensen, auto's en fietsen in de buurt. Door deze visuele meetgegevens in zowel standaard regressiemodellen als geavanceerde Random Forest-modellen te voeren, onderzocht de studie hoe de esthetiek op straatniveau vastgoedwaarden voorspelt op verschillende buurtschalen.

### Belangrijkste bevindingen
- **Groen drijft de woningwaarde op:** De Urban Greenery Index toonde de sterkste positieve invloed op vrijstaande huizen. Een toename van slechts 10% in zichtbaar groen verhoogt de huizenprijzen met ongeveer 9,4%, hoewel dit voordeel afvlakt na het bereiken van een drempel van 40%.
- **Fietsen wijzen op topappartementen:** Voor appartementen had de aanwezigheid van fietsen het sterkste positieve effect. Elke extra gespotte fiets in de buurt verhoogde de prijzen met ongeveer 10,6%, waarschijnlijk als indicator voor hoogwaardige fietsinfrastructuur en de vitaliteit van de buurt.
- **Machine learning verslaat traditie:** Het opnemen van deze uit beelden afgeleide kenmerken verbeterde de nauwkeurigheid van de waardering aanzienlijk, waarbij niet-lineaire Random Forest-modellen consequent beter presteerden dan traditionele lineaire formules.
- **Auto's verminderen de aantrekkelijkheid:** Voor alle woningtypes zorgde een hogere dichtheid van geparkeerde of rijdende auto's consequent voor een daling van de vastgoedwaarde.

### Impact
Deze bevindingen geven stedenbouwkundigen en beleidsmakers hard bewijs dat duurzaam straatontwerp economisch zinvol is. Door aan te tonen dat investeringen in groen en fietsinfrastructuur — en een vermindering van de auto-afhankelijkheid — de aantrekkelijkheid van een buurt direct vergroten, ondersteunt dit onderzoek een nauwkeurigere en eerlijkere onroerendezaakbelasting. Uiteindelijk bewijst het dat de vergroening van onze straten zich terugbetaalt, zowel voor de bewoners als voor de stad in haar geheel.
