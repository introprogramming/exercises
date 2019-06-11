#
# Palindrome checker for English words.
#
# Usage:
# python palindrome.py
#

import sys


def is_palindrome(word):
    """Returns True if argument is a palindrome, returns False otherwise."""
    word = word.lower().strip()
    if word:  # Checks that word is not empty (empty sequences are false).
        reverse_word = word[::-1]
        return word == reverse_word
    else:
        return False


def clean_string(string):
    """Removes non-letters from string leaving only ascii letters (swedish characters removed),
    whitespace and hyphens. Returns the clean string.
    """
    new_string = ""
    string.lower()
    for c in string:
        if c.isalpha() or c.isspace() or c == '-':
            new_string += c
    return new_string


def count_palindromes(text):
    """Returns the number of palindromes in a text."""
    count = 0
    text = clean_string(text)
    text = text.split()
    for word in text:
        if is_palindrome(word):
            count += 1
    return count


def palindromes_in_file(path):
    """Prints the number of palindromes in file given by path."""
    try:
        file = open(path)
        data = file.read()
        print(count_palindromes(data))
        file.close()
    except IOError as e:
        print(e.strerror)


def interactive_mode():
    """Repeatedly checks if given input from the command line are palindromes."""
    print("Input string to check. (E)xit to exit.")
    while True:
        inp = input(": ")
        if input == 'E' or input == 'e':
            print("Exiting")
            exit(0)
        else:
            inp = clean_string(inp)
            print(is_palindrome(inp))


def file_mode():
    """Repeatedly counts the palindromes in file given from the command line."""
    print("Input file name plus extension (file has to be in the same folder as python file).")
    print("(E)xit to exit.")
    while True:
        inp = input(": ")
        if inp == 'E' or inp == 'e':
            print("Exiting")
            exit(0)
        else:
            palindromes_in_file(inp)


def main():
    print("Choose mode: (I)nteractive, (R)ead from file or (E)xit.")
    while True:
        mode = input(": ")
        if mode == 'I' or mode == 'i':
            interactive_mode()
        elif mode == 'R' or mode == 'r':
            file_mode()
        elif mode == 'E' or mode == 'e':
            print("Exiting.")
            exit(0)
        else:
            print("Invalid input. (Valid inputs: I, R, E)")


if __name__ == "__main__":
    main()
