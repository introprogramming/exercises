import sys

hex_dict = \
    {'0': 0,
     '1': 1,
     '2': 2,
     '3': 3,
     '4': 4,
     '5': 5,
     '6': 6,
     '7': 7,
     '8': 8,
     '9': 9,
     'a': 10,
     'b': 11,
     'c': 12,
     'd': 13,
     'e': 14,
     'f': 15
     }


def hextodec(hex_str):
    """Works with both `ff`, `0xff` and upper-case."""
    hex_str = hex_str.lower()
    num = 0
    for char in hex_str:
        if char not in hex_dict.iterkeys():
            continue
        num *= 16
        num += hex_dict[char]
    return str(num)


def hex_char(num):
    """15->'e' etc. Inverse of hex_dict."""
    if 0 < num <= 10:
        return str(num)
    elif num < 16:
        return chr(ord('a') - 10 + num)
    else:
        raise Exception(str(num) + " is not between 0 and 15")


def dectohex(dec_str):
    dec = int(dec_str)
    hex_str = ""
    while dec > 0:
        hex_str = hex_char(dec % 16) + hex_str
        dec = dec / 16
    return "0x" + hex_str


def dectohex2(dec_str):
    """Alternative implementation using BIF"""
    dec = int(dec_str)
    return hex(dec)


if len(sys.argv) > 2:
    if sys.argv[1] == 'hex':
        print(hextodec(sys.argv[2]))
    elif sys.argv[1] == 'dec':
        print(dectohex2(sys.argv[2]))
    else:
        print("Usage: convert.py hex|dec number")
else:
    print("Usage: convert.py hex|dec number")


