#
# Robber's Language translator for Swedish words
#
# Usage:
#
# python robber.py [word|path to text file]
#
# Run without arguments to start an interactive CLI.
#
# Intentionally long source for educational purposes.
#

import mimetypes
import os
import os.path
import sys

# Helpers

CONSONANTS = "qwrtpsdfghjklzxcvbnm"
SUFFIX = 'o'


def is_consonant(char):
    """Returns true if char is consonant. False otherwise
    """
    return char.lower() in CONSONANTS.lower()


def is_valid_file(input):
    """ Returns true if input is a valid text file.
    """
    # Educational moment: Learn how use google to find about
    # Python's built in helpers for validating a path for a file
    # and checking the file type.
    return os.path.isfile(input) and mimetypes.guess_type(input)[0] == "text/plain"



def file_contents_from(path):
    """ Fetch file contents from a file at path.
    Returns False if file at path cannot be read.
    """
    try:
        f = open(path)
        return f.read()
    except IOError as e:
        return False



# Logic

def translate(string):
    """Core translation.
    """
    output = ""

    for char in string:
        output += add_suffix_if_consonant(char)

    return output


def add_suffix_if_consonant(inp):
    """Adds a suffix if input is consonant
    """
    return inp + SUFFIX + inp.lower() if is_consonant(inp) else inp



def cli():
    """ Interactive CLI. Type 'exit' to quit.
    """
    print('Type "exit" or press Ctrl+C to leave.')
    inp = _read_input()

    while inp != "exit":
        print(translate(inp))
        inp = _read_input()

    print("Bye!")


def _read_input():
    return input("Enter Swedish text: ")


def main():
    if len(sys.argv) == 2 and sys.argv[1] != "":
        inp = sys.argv[1]

        out = translate(file_contents_from(inp)) if is_valid_file(inp) else translate(inp)

        print(out)

    else:
        cli()


# Init

if __name__ == "__main__":
    # Docstring unit testing
    # import doctest
    # doctest.testmod()

    main()

    main()
