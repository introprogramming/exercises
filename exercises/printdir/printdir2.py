
import sys
import os
from os.path import isdir, getsize, join

"""Alternative implementation that uses string.format and manual recursion."""

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
    
def recurse_print(path, prefix):
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
            (string, [f_size, sub_list]) = recurse_print(f_path, prefix+"    ")
            complete_list += [(f, f_size, sub_list)]
            
            complete_string += "\n\n" + prefix + str_format(f + os.path.sep, f_size)
            complete_string += prefix+string
        else :
            f_size = file_size(path, f)
            sumsize += f_size
            complete_list.append((f, f_size))
            
            complete_string += "\n" + prefix + str_format(f, f_size)
            
    
    return (complete_string, [sumsize, complete_list])

def dir_print_contents(path):
    """Prints contents of a directory recursively.
    
    This implementation uses function recursion."""
    (string, [sumsize, sub_list]) = recurse_print(path, "")
    print string
    
def main():
    """Prints contents of directory with specified path."""
    
    path = "."
    if len(sys.argv)>1:
        path = sys.argv[1]
    
    print "In ", path, ":"
    dir_print_contents(path)

main()