#!/bin/python
# A program which uses if-cases to determine which numbers rangeing from 1 to 10 the specified integer variable is divisible by.
# here we also show the modulo operator. it gives the remainder after a divistion. example 42 % 5 = 2 since 42 = 5*x + 2

variable = 42

if variable <= 5:
    print("less than or equal to 5")

if variable % 5 == 0:
    print("divisible by 5")

if variable % 6 == 0:
    print("divisible by 6")
    
if variable % 7 == 0:
    print("divisible by 7")

