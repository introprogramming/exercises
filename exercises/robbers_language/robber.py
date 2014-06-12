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

import sys
import os
import mimetypes

# Helpers

CONSONANTS = "qwrtpsdfghjklzxcvbnm"
SUFFIX = 'o'

def is_valid_file(input):
  # Educational moment: Learn how use google to find about
  # Python's built in helpers for validating a path for a file
  # and checking the file type.
  return os.path.isfile(input) and mimetypes.guess_type(input)[0] == "text/plain"

def file_contents_from(path):
  try:
    f = open(path)
    return f.read()
  except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
    return False
  else:
    f.close()

# Logic

def translate(string):
  '''Core translation algorithm.

  >>> translate('johan')
  'jojohohanon'
  '''
  tokens = list(CONSONANTS)
  output = ""

  for char in list(string):
    output += add_suffix_if_token(char, tokens)

  return output

def add_suffix_if_token(input, tokens):
  '''Adds a suffix if input exists in tokens

  >>> add_suffix_if_token('j', list(CONSONANTS))
  'joj'
  '''
  return input+SUFFIX+input if input in tokens else input

def cli():
  input = _read_input()

  while input != "exit":
    print translate(input)
    input = _read_input()

def _read_input():
  return raw_input("Enter Swedish text: ")

def main():
  if len(sys.argv) == 2 and sys.argv[1] != "":
    input = sys.argv[1]

    out = translate(file_contents_from(input)) if is_valid_file(input) else translate(input)

    print out

  else:
    cli()


# Init

if __name__ == "__main__":
  # Docstring unit testing
  import doctest
  doctest.testmod()

  main()
