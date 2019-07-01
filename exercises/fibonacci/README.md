# Fibonacci-tal

En applikation som tar ett tal som input, och skriver ut det första [fibonacci-talet](http://en.wikipedia.org/wiki/Fibonacci_number) som är större än detta.

- **Svårighetsgrad:** 1

## Delmoment

1. Börja med en [for](https://wiki.python.org/moin/ForLoop)\-loop som skriver ut fibonacci-tal på skärmen, börja med 0, 1, 1 ... osv. Loopen behöver endast gå tillräckligt länge för att bekräfta att den skriver ut rätt talföljd (exempelvis 15 varv eller så). **Svårighetsgrad:** 1
2. Gör så att loopen, istället för att snurra ett visst antal varv, sluter när den har räknat ut ett fibonacci-tal som överstiger något tal (spelar inte så stor roll vilket tal just nu). **Svårighetsgrad:** 1
3. Låt nu användaren få mata in ett tal i terminalen och byt ut talet i förra delmomentet mot detta istället. **Svårighetsgrad:** 1
4. Ta bort utskriften av alla fibonacci-tal i loopen och skriv endast ut resultatet när det slutgiltiga talet är framtaget. **Svårighetsgrad:** 1
5. Skapa en funktion som tar emot ett argument och flytta in hela loopen. Funktionen ska returnera det värde som förut skrevs ut. Exempelvis ska `fibonacci(10)` returnera 13. **Svårighetsgrad:** 1
6. Se till så att programmet anropar funktionen med talet du får av användaren som argument och skriver ut resultatet. **Svårighetsgrad:** 1

## Utbyggnad

- Låt användaren kunna ange input-talet som ett argument till programmet, exempelvis:  
`python fibonacci.py 35`
- Prova att generera talserien [rekursivt](https://sv.wikipedia.org/wiki/Rekursion) istället för iterativt. **Svårighetsgrad:** 2
- Få programmet att fråga och svara användaren om och om igen istället för bara en gång. Spara dessutom den uträknade talserien i en lista, så att om användaren frågar om ett tal mindre än det största talet i den sparade talserien behöver talserien inte räknas ut på nytt. Istället letar man igenom listan efter svaret. Frågar däremot användaren om ett tal som är större än eller lika med det största talet i den sparade talserien så fortsätter man att generera talserien från slutet av den sparade talserien istället för att börja om på nytt. **Svårighetsgrad:** 2