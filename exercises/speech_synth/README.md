# Talsyntes

Låt datorn läsa upp text.

- **Svårighetsgrad:** 1

## Delmoment

1. Låt programmet läsa upp en lämplig sträng på engelska med hjälp av `engine.say()`.
2. Lyssna igenom de olika röster som finns tillgängliga på ert system och låt programmet använda denna med hjälp av `engine.setProperty()`.
3. Skapa en loop som låter användaren skriva in rader som programmet då läser upp. Loopen ska avbrytas av lämpligt kommando.

## Utbyggnad

- Låt användaren kunna läsa upp en text-fil genom att ange den som argument till programmet. **Svårighetsgrad:** 1
- Låt användaren kunna ändra volym, röst och hastighet utan att behöva starta om programmet.

## Externa bibliotek

- [pyttsx](http://pyttsx.readthedocs.org/en/latest/engine.html)
[Installation](http://pyttsx.readthedocs.org/en/latest/install.html)

På MacOSX räcker det med `sudo pip install pyttsx`. På windows behöver man även installera ett extra bibliotek enligt instruktioner i länk ovan.