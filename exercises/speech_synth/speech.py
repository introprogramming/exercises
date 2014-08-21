
# original:
# http://code.activestate.com/recipes/578839-python-text-to-speech-with-pyttsx/

import pyttsx

engine = pyttsx.init()


def listen_to_voices():
    """Listen to available voices on your system. Choose one to be used in init()."""
    voices = engine.getProperty('voices')
    i = 0
    for voice in voices:
        print "Using voice:", repr(voice)
        engine.setProperty('voice', voice.id)
        engine.say("Hi there.")
        engine.say("I am number %s" % str(i))
        i = i+1

def init():
    """Set voice properties."""
    engine.setProperty('rate', 190)
    engine.setProperty('volume', 1.0)
    engine.setProperty('voice', engine.getProperty('voices')[18].id)

def say_something(line):
    engine.say(line)
    engine.runAndWait()



init()
#listen_to_voices()

print "Exit by typing `exit` or simply an empty line ``"

say_something("At your command...")

line = raw_input("Say something: ")
while line != "" and line != "exit":
    say_something(line)
    line = raw_input("Say something: ")
