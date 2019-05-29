# Rövarspråk

**Svårighetsgrad:** 1

Skriv ett program som översätter från svenska till [rövarspråket](http://sv.wikipedia.org/wiki/R%C3%B6varspr%C3%A5ket)!

## Delmoment

1. Skriv en metod som översätter en given sträng till rövarspråket **Svårighetsgrad 1**

    Exempel: om funktionen heter `to_robbers_language`:
    ```python
    print(to_robbers_language("Hejsan"))
    ```
    ska till exempel ge följande utskrift i konsollen:
    ```bash
    HoHejojsosanon
    ```

2. Lägg nu till så att programmet kan kallas med ett argument från kommandoraden och då skriva ut översättningen av argumentet.
   **Svårighetsgrad 1**
   
   Exempel: om filen heter `robber.py`:
   ```bash
    python robber.py Hejsan
    HoHejojsosanon
    ```

3. Gör nu så att programmet vid utelämnande av argument istället kontinuerligt frågar användaren efter nya ord att översätta.
    **Svårighetsgrad 1**

      ```bash
      python robber.py
      Hi! What do you want to translate?
      > Johan
      The translation is:
      Jojohohanon
      > Hästar är fina.
      The translation is:
      HoHäsostotaror äror fofinona.
      ...
      ```
3. Gör nu så att programmet givet ett argument som är en sökväg till en fil skriver ut översättningen av filens innehåll. Om argumentet inte är en sökväg till en fil ska som tidigare översättningen av argumentet skrivas ut.
    **Svårighetsgrad 2**
    
    Exempel: om skript-filen heter `robber.py` och filen `text_file` innehåller följande text:
    `En kort textfil`
    ```bash
    python robber.py text_file.txt
    Translating from 'text_file.txt':
    Enon kokorortot totexoxtotfofilol
    ```
  
## Om rövarspråket

> Rövarspråket (rorövovarorsospoproråkoketot) är ett enkelt kodspråk som framför allt används av barn. Det blev populärt i och med Astrid Lindgrens romaner om Kalle Blomkvist. Idén till rövarspråket ska ha kommit från Astrids make, Sture Lindgren, som använde det i lek med sina kamrater som barn. Eftersom rövarspråket har en enkel struktur som är lätt att avkoda passar sig språket inte i skriven form. Men i talad form kan det vara svårt för en oinsatt att förstå vad som sägs, särskilt om det talas snabbt.

[Wikipedia](http://sv.wikipedia.org/wiki/R%C3%B6varspr%C3%A5ket)

Regeln för rövarspråket är att man efter varje konsonant lägger ett o (kort å-ljud) och därefter samma konsonant igen, till exempel byts b ut mot "bob" och f mot "fof". Vokalerna är oförändrade. "Jag talar rövarspråket" blir alltså "jojagog totalolaror rorövovarorsospoproråkoketot".
