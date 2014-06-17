
import sys
import os
from os.path import getsize, join

def dir_contents_size(path):
    """Prints how many bytes a directory contains.
    
    Shamelessly copied from https://docs.python.org/2/library/os.html#os.walk"""
    for root, dirs, files in os.walk(path):
        print root, "consumes",
        print sum(getsize(join(root, name)) for name in files),
        print "bytes in", len(files), "non-directory files"

def dir_print_contents(path):
    """Prints contents of a directory recursively.
    
    This implementation uses standard functions for iterating."""
    for root, dirs, files in os.walk(path):
        print ""
        print root + os.sep
        for file in files:
            print "\t"+file+"\t", getsize(join(root, file)), "bytes"

def main():
    """Prints contents of directory with specified path."""
    path = "."
    if len(sys.argv)>1:
        path = sys.argv[1]
    
    print "In ", path, ":"
    dir_print_contents(path)

main()