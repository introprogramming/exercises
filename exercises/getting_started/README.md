# Programflöde, primtal och den magiska modulo operatorn

I denna uppgift får du lära dig om:
- logiska satser
- loopar
- funtioner

**Svårighetsgrad:** 1

## Delmoment

1. Undersök loop.py, if.py, if_else.py,
	I de ovan nämnda filerna finns kod som demonstrerar hur loopar och if-satser fungerar.
	
	Börja med att köra loop.py
	Undersök nu vad som händer om du ändrar parametern till range funktionen på rad 4 från 10 till något annat tal.

	Fortsätt nu med att köra de två filerna if.py och if_else.py.
	Se till att du förstår skillnaden mellan flera if-satser och en stor if-else sats.
	Diskutera det gärna med en handledare om du är osäker.

2. Undersök fizzbuzz.py,
	Läs igenom specifikationen i fizzbuzz.py för att se hur fizzbuzz ska fungera.
	Testa att köra fizzbuzz.py. Notera att "FizzBuzz" aldrig skrivs ut.
	Det är något som är fel på if-else satsen. Försök lösa problemet.
	Tips: programmet körs linjärt. Tänk på vad som händer rad för rad.

3. Funktioner har du redan sett och använt, exempelvis print("Hello, World!") eller range(10), dock är det här första gången som du ser hela definitionen på en.
	Du kan själv definiera funktioner genom att skriva

	def funktionsnamn(parameter1, parameter2):
		funktionskropp

	funktionsnamn innehåller vanligtvis små och stora bokstäver samt '_'.
	parameterlistan (det innanför parenteserna) kan innehålla hur många parametrar som helst men behöver heller inte ha några alls. parametrar separeras med ','.
	
	Var som helst i en funktion kan man använda 'return x', funktionen returnerar då x och avbryts direkt. Resten av programmet körs vidare där funktionen kallades.
	
	När man skriver små program kanske man inte behöver funktioner. Men när det börjar bli större så är de väldigt användbara för att strukturera upp koden och göra abstraktioner. Man kan tänka på en funktion som en låda där du stoppar in något på ena sidan och får ut något på andra, likt en funktion i matematiken.

	I functions.py ser du några exempel på hur funktioner fungerar. Du behöver inte memorera allt nu, du kan återkomma och se hur syntaxen ser ut, det viktiga är att du förstår vilka möjligheter det ger dig.

4. Funktionen "contains" och listor.
	Listor finns i de flesta programmeringsspråk. lists.py innehåller exempel och övningar på hur listor kan användas.

	När du är nöjd och har fått lite förståelse för hur listor fungerar gå vidare till contains.py.
	Undersök hur contains funktionen fungerar och skriv sedan färdigt sublist_contains.

5. Härnäst ska vi beräkna primtal.
	prime.py innehåller en funktion för att kolla om ett tal är ett primtal. Funktionen är dock inte helt färdigskriven.
	Funktionen säger att alla tal under 2 är primtal eftersom range(2,x) ger en tom lista om x < 2. Detta leder till att funktionen returnerar True.

	Skriva ut all primtal under 100.
	Använd en for-loop för att iterera över alla tal mellan 0 och 100,
	använd sedan en if-sats som kollar resultatet från is_prime funktionen och skriv ut talet om det är ett primtal.

	Skapa en funktion som du kallar för print_primenumbers_less_than(x). Låt funktionen ta en parameter x och lägg din redan skrivna logik i denna funktion.
	Se till så att din logik istället skriver ut alla primtal upp till x.



När du har klarat dessa övning bör du ha kunskap om:
 * if och if-else satser
 * for-loopar
 * listor
 * funktioner, parameterlistor och returvärden


