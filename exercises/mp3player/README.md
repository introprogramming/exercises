# Mp3-spelare

Ett program som spelar upp musik-filer som mp3 och wav.

- **Svårighetsgrad: 1**

*Felsökning:*

- Om musiken spelas upp men i fel hastighet kan man ange 'sample rate' mha `pygame.mixer.music.init(44100)`.
- Om det kommer upp ett felmeddelande "Unrecognized music format" trots att det är .mp3, så testa med en .ogg eller .wav istället. Pygame skriver att deras läsning av mp3 kan strula på vissa platformar.
- Funktionerna `rewind()` och `queue()` i `pygame.mixer.music` verkar vara lite instabila.
- Pyglet stödjer i första hand .wav.

## Delmoment

1. Importera pygame's musik-bibliotek, [pygame.mixer.music](http://www.pygame.org/docs/ref/music.html). Använd funktionen `load()` för att ladda in en musik-fil. **Svårighetsgrad 1**
2. Vid `play()` så kommer den laddade filen att börja spelas upp. Programmet kommer dock att avslutas innan den hinner spela färdigt (eller ens börja spela). Därför behöver programmet vänta på input från användaren innan den får stängas av. Använd standard-funktionen `raw_input()` för detta. **Svårighetsgrad 1**

## Utbyggnad
* Låt användaren välja vilken fil som ska spelas upp genom att ange det som ett argument till programmet:  
`python mitt_program.py "en fin sång.mp3"` **Svårighetsgrad 1**
* Låt användaren kunna pausa musiken eller spela upp en annan sång. Dessa finns som funktioner i `pygame.mixer.music`. **Svårighetsgrad 2**

## Externa bibliotek
Är man ganska ny som programmerare rekommenderas pygame (som också används i flera andra uppgifter). Vill man lägga ner väldigt mycket tid på denna uppgiften för att skapa en grafiskt snygg mp3spelare så använd pyglet.

* [pygame](http://www.pygame.org/)

alternativt

* [pyglet](http://www.pyglet.org/download.html)

**OBS!** Pyglet kräver 32-bit Python för att fungera.  
Kort pyglet [guide](http://www.pyglet.org/doc/programming_guide/writing_a_pyglet_application.html).