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

def is_consonant(char):
  '''Returns true of char is consonant. False otherwise

  >>> is_consonant('a')
  False
  >>> is_consonant('d')
  True
  '''
  return char.lower() in CONSONANTS.lower()

def is_valid_file(input):
  ''' Returns true if input is a valid text file.

  >>> is_valid_file('./fixtures/test.txt')
  True
  >>> is_valid_file('./bogus')
  False
  '''
  # Educational moment: Learn how use google to find about
  # Python's built in helpers for validating a path for a file
  # and checking the file type.
  return os.path.isfile(input) and mimetypes.guess_type(input)[0] == "text/plain"

def file_contents_from(path):
  ''' Fetch file contents from a file at path.
  Returns False if file at path cannot be read.

  >>> file_contents_from('./fixtures/test.txt')
  'En enkel fil.\\n'
  >>> file_contents_from('./bogus')
  False
  '''
  try:
    f = open(path)
    return f.read()
  except IOError as e:
    return False
  else:
    f.close()

# Logic

def translate(string):
  '''Core translation.

  >>> translate('johan')
  'jojohohanon'
  '''
  output = ""

  for char in list(string):
    output += add_suffix_if_consonant(char)

  return output

def add_suffix_if_consonant(input):
  '''Adds a suffix if input is consonant

  >>> add_suffix_if_consonant('j')
  'joj'
  >>> add_suffix_if_consonant('a')
  'a'
  '''
  return input+SUFFIX+input.lower() if is_consonant(input) else input

def cli():
  ''' Interactive CLI. Type 'exit' to quit.
  '''
  print 'Type "exit" or press Ctrl+C to leave.'
  input = _read_input()

  while input != "exit":
    print translate(input)
    input = _read_input()

  print "Bye!"

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
