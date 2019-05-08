#!/bin/python


def contains(input_list, e):
    """ determines whether e is contained in the list """
    for elem in input_list:  # elem is short for element (an item in the list)
        if elem == e:
            return True
    return False


integer_list = [0, 1, 2, 3]

print("")
print("Does the list contain 3?:", contains(integer_list, 3))
print("Does the list contain 5?:", contains(integer_list, 5))
print("")

list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4, 5, 6, 7]
list3 = [1, 2, 3, 5]

# Create a function which determines whether all elements in a list are
# contained in another list.
# Some tips:
# - Use the contains function defined above.
# - You want to check if each element in the sublist is contained in the list
# - You can use boolean arithmetic, see the examples in boolean_arithmetic.py


def sublist_contains(list, sublist):
    # Your code goes here
    return None


# Some tests to make sure your function works. The value that your function
# returns should match the expected value.
print("")
print("Expected True,  Actually got:", sublist_contains(list2, list1))
print("Expected False, Actually got:", sublist_contains(list3, list1))
print("Expected True,  Actually got:", sublist_contains(list1, list1))
print("")
