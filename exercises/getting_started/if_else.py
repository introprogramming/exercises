#!/bin/python
# A program to show the difference between mulitple if-statements and a larger if-else-statement (see also if.py).

variable = 42

if variable <= 5:
    print("less than or equal to 5")
elif variable % 5 == 0:
    print("Divisible by 5")
elif variable % 6 == 0:
    print("Divisible by 6")
elif variable % 7 == 0:
    print("Divisible by 7")
else:
    print("Not less than or equal to 5 nor divisible by any number in the range [5-7]")
