
import sys
import datetime

########################
## Functions

def clean(string):
    """Return a *clean* string
    
    Removes whitespace and hyphen
    """
    return string.replace(" ", "").replace("-", "")

def date_is_correct(string):
    """Return True or False
    
    Checks if the string follows "--MMDD..." format and if the date exist
    """
    try:
        datetime.datetime.strptime(string[2:6], '%m%d')
    except ValueError:
        return False
    return True

def string_to_int_list(string):
    """Return list of integers
    
    Converts a string of integer characters to a list of integers
    '1234' -> [1,2,3,4]
    """
    return map(int, list(string))
    
    
def number_is_correct(pnr):
    """Returns True or False
    
    Checks that the social security control number is valid
    """
    factor = 2
    c = 0
    for x in pnr :
        c = c + x*factor
        if(x*factor > 9):
            c = c -9
        
        if factor == 2:
            factor = 1
        else :
            factor = 2
    return c % 10 == 0

def check(str):
    """Returns (True/False, Explanation)
    
    Checks if a social security number is valid by checking date and control number
    """
    cleaned = clean(pnr)

    if len(cleaned) != 10:
        return (False, 'The personal number must include ten digits')
    
    if not date_is_correct(cleaned):
        return (False, 'Error in date')

    if not number_is_correct(string_to_int_list(cleaned)):
        return (False, 'Error in control number')

    return (True, 'Congratulations, the number is correct')

########################
## Main

pnr = "811218-9876"

if len(sys.argv) > 1:
    pnr = sys.argv[1]
else:
    print "Uses default number: ", pnr

a = check(pnr)

print a[1]
