
# original:
# http://code.activestate.com/recipes/578839-python-text-to-speech-with-pyttsx/

import pyttsx
engine = pyttsx.init()
engine.setProperty('rate', 70)

voices = engine.getProperty('voices')
for voice in voices:
    print "Using voice:", repr(voice)
    engine.setProperty('voice', voice.id)
    engine.say("Hi there.")
engine.runAndWait()