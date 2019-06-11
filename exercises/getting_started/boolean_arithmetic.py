#!/bin/python

# The boolean operators are not, and, or
# Can you see how they work?
print("not True:       ", (not True))
print("True and True:  ", (True and True))
print("True and False: ", (True and False))
print("True or False:  ", (True or False))
print("False or False: ", (False and False))
print("")

# Assigning a boolean value to a variable
boolean_variable = True

# You can reassign a variable
boolean_variable = False
boolean_variable = boolean_variable or True

# Usage in if-else-statement
if boolean_variable:
    print("boolean_variable is True")
else:
    print("boolean_variable is False")
