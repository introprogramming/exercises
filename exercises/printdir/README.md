
#Printdir

Skriv ett program som skriver ut vad en mapp innehåller och hur mycket plats varje fil tar samt upprepa detta för mappens undermappar. Programmet ska läsa in vilken sökväg som ska undersökas.
För denna uppgifts kan det vara bra att använda sig av rekursion.

- **Svårighetsgrad:** 1

## Delmoment

1. Läs in en sökväg till en mapp (path). **Svårighetsgrad 1**
2. Skriv ut vilka filer den innehåller och deras respektive storlek, för detta kan det vara bra att använda sig av [os.path](https://docs.python.org/2/library/os.path.html). **Svårighetsgrad 1**
3. Upprepa för undermappar (subdirectories). **Svårighetsgrad 1**

## Utbyggnad

- Använd string.format(...) för att formattera utskriften så att det blir fina kolumner. **Svårighetsgrad 1**
- Efter mappens namn: skriv ut respektive mapps samlade storlek (summa av innehåll). **Svårighetsgrad 2**
- Låt användaren lägga till ett `regex pattern` som filerna och eller mapparna ska följa för att skrivas ut. **Svårighetsgrad 2**
- Lägg till argumentflaggor som -h eller -f etc som gör olika saker. Låt `-h` flaggan skriva ut en lista över alla flaggorna, deras användning samt deras funktion. **Svårighetsgrad 2**
- Låt användaren utföra en operation på filerna som att kopiera eller byta namn på dem. *Obs! Testa inte detta på mappar med värdefullt innehåll. Testa alltid på kopior först!*  **Svårighetsgrad 2**

## Externa bibliotek
- (inga)
