# MIDI keyboard

Att bygga ett "mjukvaru-piano" eller s.k. MIDI-keyboard med ca 14 tangenter (c1-e2). När man trycker ner en tangent ska det motsvara att trycka ner en tangent på en synth (och låta genom högtalarna).

- Svårighetsgrad 2?

## Moment
1. Spela upp ett inprogrammerat MIDI-ljud på datorn.
2. Läs in tangentnedtryckningar med `pygame event` och slå på/av respektive ton.

## Utbyggnad
- Lägg till funktionalitet att spela in musiken till en fil.
- Spela upp ljud från midi-filer.
- Funktionalitet för att byta oktav med exempelvis 'z' och 'x'.

## Externa bibliotek
Finns flera att välja mellan. Inte minst pygame, python-rtmidi och Mido. Använder förmodligen pygame för smidighetens skull (då det även används till många andra övningar).
