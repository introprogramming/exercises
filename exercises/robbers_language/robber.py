import sys

# Helpers

CONSONANTS = "qwrtpsdfghjklzxcvbnm"
SUFFIX = 'o'

def is_path(input):
  return

def file_contents_from(path):
  return

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
  return

def main():
  if len(sys.argv):
    input = sys.argv[1]

    out = translate(file_contents_from(input)) if is_path(input) else translate(input)

    print out

  else:
    cli()


# Init

if __name__ == "__main__":
  # Docstring unit testing
  import doctest
  doctest.testmod()

  main()
