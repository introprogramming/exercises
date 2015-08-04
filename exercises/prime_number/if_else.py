#!/bin/python
# A program just to show the difference between mulitple if-statements and a larger if-else-statement

variable = 42

if variable % 2 == 0:
    print("Divisible by 2")
elif variable % 3 == 0:
    print("Divisible by 3")
elif variable % 4 == 0:
    print("Divisible by 4")
elif variable % 5 == 0:
    print("Divisible by 5")
elif variable % 6 == 0:
    print("Divisible by 6")
elif variable % 7 == 0:
    print("Divisible by 7")
elif variable % 8 == 0:
    print("Divisible by 8")
elif variable % 9 == 0:
    print("Divisible by 8")
elif variable % 10 == 0:
    print("Divisible by 8")
else:
    print("Not divisible by any number int the range [2-10]")
