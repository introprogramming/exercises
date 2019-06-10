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

  >>> is_consonant('a')
  False
  >>> is_consonant('d')
  True
  """
    return char.lower() in CONSONANTS.lower()


def is_valid_file(inp):
    """ Returns true if input is a valid text file.

  >>> dir_path = os.path.split(os.path.abspath(__file__))[0]
  >>> is_valid_file(dir_path + os.path.sep + 'fixtures' + os.path.sep + 'test.txt')
  True
  >>> is_valid_file('./bogus')
  False
  """
    # Educational moment: Learn how use google to find about
    # Python's built in helpers for validating a path for a file
    # and checking the file type.
    return os.path.isfile(inp) and mimetypes.guess_type(inp)[0] == "text/plain"


def file_contents_from(path):
    ''' Fetch file contents from a file at path.
  Returns False if file at path cannot be read.

  >>> dir_path = os.path.split(os.path.abspath(__file__))[0]
  >>> file_contents_from(dir_path + os.path.sep + 'fixtures' + os.path.sep + 'test.txt')
  'En enkel fil.\\n'
  >>> file_contents_from('./bogus')
  False
  '''
    try:
        f = open(path)
        return f.read()
    except IOError as e:
        return False


# Logic

def translate(string):
    """Core translation.

  >>> translate('johan')
  'jojohohanon'
  """
    output = ""

    for char in string:
        output += add_suffix_if_consonant(char)

    return output


def add_suffix_if_consonant(input):
    """Adds a suffix if input is consonant

  >>> add_suffix_if_consonant('j')
  'joj'
  >>> add_suffix_if_consonant('a')
  'a'
  """
    return input + SUFFIX + input.lower() if is_consonant(input) else input


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
        input = sys.argv[1]

        out = translate(file_contents_from(input)) if is_valid_file(input) else translate(input)

        print(out)

    else:
        cli()


# Init

if __name__ == "__main__":
    # Docstring unit testing
    import doctest

    doctest.testmod()

    main()
