
import sys

if sys.maxsize > 2**32:
    print "using 64 bits"
else:
    print "using 32 bits"