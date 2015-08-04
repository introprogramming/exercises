#!/bin/python


def is_prime(integer):
    """Determines weather integer is prime, returns a boolean value"""
    for i in range(2, integer):
        if integer % i == 0:
            return False 
    return True



# Your code below:
print("Should be False (0): %r" % is_prime(0))
print("Should be False (1): %r" % is_prime(1))
print("Should be True  (2): %r" % is_prime(2))
print("Should be False (8): %r" % is_prime(8))
print("Should be True (17): %r"% is_prime(17))
