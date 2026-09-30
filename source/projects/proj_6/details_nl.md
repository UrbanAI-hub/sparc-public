### Overzicht
Veroorzaakt een gevaarlijk ogend kruispunt daadwerkelijk meer ongevallen? Dit project onderzoekt of het formaliseren van de "visuele veiligheidsindruk" van verkeersexperts naar een schaalbaar computer vision-model de voorspelling van ongevallen in het wegennet van Rotterdam kan verbeteren in vergelijking met traditionele verkeersvolumemodellen.

### De uitdaging
Het evalueren van de veiligheid van kruispunten is van oudsher een handmatig en tijdrovend proces dat afhankelijk is van bezoeken door experts ter plaatse. Hoewel stedenbouwkundigen en ingenieurs een sterk intuïtief gevoel hebben voor wat een kruispunt er gevaarlijk uit laat zien, is het onmogelijk om dit menselijke oordeel op te schalen naar een hele stad. De uitdaging is bepalen of kunstmatige intelligentie deze visuele intuïtie kan leren uit beelden op straatniveau en, nog belangrijker, of dat visuele gevaar daadwerkelijk nieuwe voorspellende waarde toevoegt aan de standaard verkeersgegevens.

### Doelstellingen
* **Verzamelen en formaliseren** van de visuele veiligheidsoordelen van verkeersingenieurs via paarsgewijze beeldvergelijkingen.
* **Trainen van een computer vision-model** om deze subjectieve expertscores op te schalen naar alle kruispunten in Rotterdam.
* **Evalueren** of deze nieuwe visuele veiligheidsmaatstaf de nauwkeurigheid van conventionele voorspellingsmodellen voor ongevallen verbetert.

### Aanpak
Het onderzoeksteam verzamelde Google Street View-beelden van kruispunten in heel Rotterdam. Ze voerden een expertstudie uit waarbij verkeersingenieurs herhaaldelijk het 'gevaarlijkste' kruispunt kozen uit beeldparen. Dit creëerde een robuuste basis van menselijke oordelen. Een computer vision-model werd vervolgens getraind om deze scores te repliceren en te generaliseren naar het hele stadsnetwerk. Tot slot werden deze door AI gegenereerde visuele risicoscores geïntegreerd in traditionele statistische ongevalmodellen — die gebaseerd zijn op variabelen als verkeersvolume en snelheid — om te zien of de visuele data extra voorspellende waarde bood.

### Belangrijkste bevindingen
* **AI kan expertintuïtie aanleren:** Het computer vision-model slaagde erin de visuele veiligheidsscores van de menselijke verkeersingenieurs over het netwerk met redelijke nauwkeurigheid te repliceren.
* **Beeld weerspiegelt volume:** Hoewel het 'gevaar' nauwkeurig werd vastgelegd, verbeterde de visuele score de voorspellingen van daadwerkelijke ongevallen niet. Visueel gevaar en verkeersvolume zijn namelijk sterk met elkaar verweven; een kruispunt dat er 'gevaarlijk uitziet', is meestal gewoon een erg drukke, brede weg.
* **Traditionele modellen blijven sterk:** De visuele veiligheidsscore hercodeert grotendeels de indicatoren voor blootstelling en snelheid die traditionele ongevalmodellen al perfect meenemen.

### Impact
Voor de gemeente Rotterdam is dit onderzoek een sterke bevestiging dat hun huidige datagestuurde aanpak voor netwerkscreening (gebaseerd op verkeersvolume en snelheid) al optimaal is. Dit bespaart de stad hoge investeringen in overbodige technologieën voor visuele beoordelingen ter classificatie. Het onderzoek onthulde echter een verrassende tweede toepassing: omdat de visuele score van de AI het verkeersvolume zo nauwgezet volgt, kan deze dienen als een voordelige proxy om de verkeersintensiteit te schatten in steden of op nieuwe kruispunten waar officiële verkeersgegevens ontbreken.
