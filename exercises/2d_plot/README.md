#2d plot

## Svårighetsgrad: 3

## Moment
1. Rita en linje i ett fönster med 640x480 pixlar mha `pygame.draw.line(...)`, dvs få grafiken att överhuvudtaget fungera.
2. Antag ett koordinatsystem med y positivt uppåt och x positivt åt höger, dvs som man brukar rita dem i matten. Skapa en funktion för att omvandla en koordinat i detta system till en "pixel-position" i fönstret (dvs y positiv nedåt). Denna kan lätt kontrolleras mha att rita linjer enligt 1. Till exempel `[0,0]` -> `[0,480]`.
3. I omvandlingsfunktionen: ta nu även hänsyn till skala - gör så att fönstret utgör området `0<x<10` och `0<y<10` snarare än `0<x<640` etc. Till exempel `[5,0]` -> `[320, 480]`.
4. Skapa en funktion som omvandlar en matematisk funktion `f` till `N` koordinater `[x, y]` med jämna mellanrum. Till exempel `f(x)=2*x` -> `[[0,0],[1,2],...,[5,10]]`
5. Omvandla de `N` koordinaterna till en lista av pixel-positioner.
6. Rita ut funktionen genom att stoppa in listan av positioner till `pygame.draw.lines(...)`

## Utbyggnad
* Anpassa så att fönstret går från `x_min < x < x_max` istället för `0 < x < 10`
* Rita ut koordinat-axlarna
* Rita rutnät eller markeringar på koordinat-axlarna.
* Rita flera funktioner

## Externa bibliotek:
* [pygame](http://www.pygame.org/news.html)