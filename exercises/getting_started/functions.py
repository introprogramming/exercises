#!/bin/python
# import statement needed to access code and functions located in other files.
import random


def my_function():
    """ A function with no parameters, only a return value. """
    return 42


def boolean_function(bool_variable):
    """ A function with one parameter which is used to determine what to return """
    if bool_variable:
        return "The boolean variable is True"
    else:
        return "The boolean variable is False"


def print_my_coords(x=0, y=0):
    """ A function with 2 parameters and no return value.
    It also has default values for both parameters, these are used if you don't
    pass a value yourself """
    print("Coordinates ({},{})".format(x, y))


print("my_function returns:", my_function())
print("boolean_function returns:", boolean_function(True))
print("boolean_function returns:", boolean_function(False))

print_my_coords(2, 5)
print_my_coords(2)
print_my_coords(y=5)
print_my_coords()
