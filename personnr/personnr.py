
import sys
import datetime

########################
## Functions

def clean(string):
    ix  = 0
    list = []
    for char in string:
        if char != '-' and char != ' ':
            list = list + [int(char)]
    return list

def date_is_correct(pnr):
    string = ''
    for i in pnr[2:6] :
        string = string + str(i)
    #print string
    try:
        datetime.datetime.strptime(string, '%m%d')
    except ValueError:
        return False
    return True

def number_is_correct(pnr):
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

    #print c
    return c%10==0

def check(str):
    cleaned = clean(pnr)
    print cleaned

    L = len(cleaned)
    if L != 10:
        return (False, 'The personal number must include ten digits')

    if not date_is_correct(cleaned):
        return (False, 'Error in date')

    if not number_is_correct(cleaned):
        return (False, 'Error in number')

    return (True, 'Congratulations, the number is correct')

########################
## Main

pnr = "811218-9876"
#print sys.argv
if len(sys.argv)>1:
    pnr = sys.argv[1]
else :
    print "Uses default number: ", pnr

a = check(pnr)

print a[1]
