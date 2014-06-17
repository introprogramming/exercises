
import sys
import os
from os.path import isdir, getsize, join
import re

"""Alternative implementation that uses string.format and manual recursion.

Also supports regex for files and directories."""

def file_size(root, file):
    """Simply returns the file size of the `file` in directory `root`"""
    return getsize(join(root,file))

def size_to_str(size):
    """Returns printable string representation of a file's size."""
    units = ['bytes', 'kB', 'MB', 'GB', 'TB']
    ix = 0
    is_int = True
    
    while size > 1024:
        is_int = False
        size = float(size)/1024
        ix = ix + 1
    
    if is_int:
        return "{0:>4} {1}".format(size, units[ix])
    else:
        return "{0:>4.2f} {1}".format(size, units[ix])

def str_format(path, size):
    """Formats output of name and size of files and directories."""
    return "{0:<24} {1}".format(path, size_to_str(size))
    
def recurse_print(path, prefix, file_reg, dir_reg):
    """Returns (printable_string, [sum_bytes, data]).
    
    Path = path to search in.
    Prefix = string preceding each line entry in the printable_string.
    
    Recurses through the file tree. Thus creates large overhead and consumes much memory.
    
    The printable_string is formatted already for easy printing. The sum_bytes is the sum of the size of all files in the directory and subdirectories.
    
    The `data` object contains a tree structure of the names and sizes of all files in this directory and subdirectories."""
    complete_list = []
    complete_string = ""
    sumsize = 0
    
    for f in os.listdir(path):
        f_path = join(path, f)
        if isdir(f_path):
            if not dir_reg.search(f) :
                print "Dir regex didn't match", f
                continue
            
            (string, [f_size, sub_list]) = recurse_print(f_path, prefix+"    ", file_reg, dir_reg)
            complete_list += [(f, f_size, sub_list)]
            
            complete_string += "\n\n" + prefix + str_format(f + os.path.sep, f_size)
            complete_string += prefix+string
        else :
            if not file_reg.search(f) :
                print "File regex didn't match", f
                continue
            f_size = file_size(path, f)
            complete_list.append((f, f_size))
            
            complete_string += "\n" + prefix + str_format(f, f_size)
        sumsize += f_size
    
    return (complete_string, [sumsize, complete_list])

def dir_print_contents(path, file_reg, dir_reg):
    """Prints contents of a directory recursively.
    
    This implementation uses function recursion."""
    (string, [sumsize, sub_list]) = recurse_print(path, "", file_reg, dir_reg)
    print "\n"+str_format(path + os.path.sep, sumsize)
    print string

def experiment():
    """Just for experimenting on regex."""
    reg = re.compile("txt$")
    strings = ["a.txt", "a", "txt", ".txt", "c.a.txt.a"]
    
    for s in strings:
        if reg.search(s):
            print "Matches", s
        else:
            print "No match", s

def help_format(option, text):
    return "\n\t{0:<15}{1}".format(option, text)

def print_help():
    print """Printdir2
    This is a program for printing of files and calculating the sizes of directories.

    Is called by typing `python printdir2.py [path] [options]`.
    
    Options:""" +\
    help_format("-h", "Print this help and abort.") +\
    help_format("-f <regex>", "Only consider files matching this regex.") +\
    help_format("-r <regex>", "Only consider directories matching this regex.")
    
    
def main():
    """Prints contents of directory of specified path.
    
    Options:
    -f [file_regex]
    -r [dir_regex]"""
    
    path = "."
    
    #Can specify default regex here, also reads regex from program arguments.
    file_reg = "^(?!README)"
    dir_reg = "^(?!.git)"
    
    ix = 1
    while ix < len(sys.argv):
        flag = sys.argv[ix]
        if flag == '-f':
            file_reg = sys.argv[ix+1]
            ix =  ix+1
        elif flag == '-r':
            dir_reg = sys.argv[ix+1]
            ix =  ix+1
        elif flag == '-h':
            print_help()
            return
        else:
            path = sys.argv[ix]
        ix = ix+1
    
    print "File reg: " + repr(file_reg)
    print "Dir reg: " + repr(dir_reg)
    
    print "\nIn ", path, ":"
    dir_print_contents(path, re.compile(file_reg), re.compile(dir_reg))

main()

#experiment()