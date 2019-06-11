#
# Decimal to binary (and back) converter 
#
# Usage:
# python convert.py bin|dec 100
#

import sys

def dectobin(dec_string):
	"""Convert a decimal string to binary string"""
	bin_string = bin(int(dec_string))
	return bin_string[2:]

def bintodec(bin_str):
	"""Convert a binary string to decimal string"""
	num = 0
	index = 1
	for c in reversed(bin_str):
		num = num + index * int(c)
		index = index * 2
	return num

if len(sys.argv) > 2:
	if sys.argv[1] == 'bin':
		print(bintodec(sys.argv[2]))
	elif sys.argv[1] == 'dec':
		print(dectobin(sys.argv[2]))
	else:
		print("Usage: convert.py bin|dec number")
else:
	print("Usage: convert.py bin|dec number")
