# Tic-Tac-Toe

Spelet Tic-Tac-Toe eller tre-i-rad som många kallar det:
Två spelare som ska turas om att lägga kryss (X) resp. nolla (O) på ett (3x3) rutnät . Spelaren som först får tre i rad vinner. 
Programmet läser in vilken ruta man vill placera sitt tecken på och lägger därefter spelarens markör på rutan.

- **Svårighetsgrad:** 1

## Delmoment
0. Fördelaktigt att ha gjort control_flow uppgiften men inget krav.  
**Svårighetsgrad 1**

1. Skapa ett rutnät för spelet i konsollen och skriv en funktion printGameArea() som visar en tom 3x3 spelplan.  
**Tips**: Gör det enkelt, använd lista med 9 element. Testa hårdkoda in tecknen och printa ut.  
**Svårighetsgrad 1**

2. Skapa en funktion placeSign() som givet en position (1-9) och tecken sätter tecknet på rätt position i rutnätet  **Svårighetsgrad 1**.

3. Ha en play() funktion där spellogiken ligger. Byt tur mellan två spelare och använd dig av föregående funktion för att sätta ut tecknen.  
 **Svårighetsgrad 1**.

4. Modifiera funktionen placeSign() så att den hanterar felaktig position, t.ex utanför rutnätet eller att en position är redan upptagen och istället ber spelaren om en ny position.  
**Svårighetsgrad 1**.

5. Skapa en funktion hasThreeInRow() som tar in ett tecken och avgör om man har vunnit. 
Tips: Skriv alla möjliga fall för enkelhetens skull. Alternativt skriv en algoritm som gör det automatiskt.   
**Svårighetsgrad 1**.

6. Modifiera funktionen play() som nu ska använda sig av hasThreeInRow() dvs man ska kunna vinna.  
 **Svårighetsgrad 1**.

7. Modifiera funktionen play() så att det kan bli oavjort.  
 **Svårighetsgrad 1**.

## Externa bibliotek
*(inga)
