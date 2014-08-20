import sys
import pyglet
from pyglet.window import key

# Pyglet implementation
#
# DEPRECATED!
# We don't intend on using Pyglet in the course anylonger.
#
# Doesn't work so well with the sample.wav :P
# Only supports WAV unless one also installs AVBin

file = 'sample2.wav'
if len(sys.argv)>1:
    file = sys.argv[1]

window = pyglet.window.Window()

music = pyglet.resource.media(file)

player = pyglet.media.Player()
player.queue(music)
player.play()

paused = False

def help():
    print """\nCommands:
\tEsc or x \t Exit program
\tp \t Pause/unpause music
\th \t See this list again"""

print """Welcome to this music player!

You can give a file as an argument or use the commands below."""
help()

@window.event
def on_key_press(symbol, modifiers):
    global paused
    global player
    global window
    
    if symbol == key.P:
        if paused:
            print "Resume"
            player.play()
            paused = False
        else:
            print "Pause"
            player.pause()
            paused = True
    elif symbol == key.R:
        pass
        #Doesn't work :P
        #player.seek(0)
    elif symbol == key.H:
        help()
    elif symbol == key.ESCAPE or symbol == key.X:
        window.close()

pyglet.app.run()

pyglet.app.exit()

# Unimplemented features
# - need user input to be useful
while False:
    if s == "q" or s == "queue":
        file = raw_input("Add file to queue: ")
        music = pyglet.resource.media(file)
        player.queue(music)
    elif s == "n" or s == "next":
        player.next()
    elif s == "pl" or s == "play":
        file = raw_input("Play this file instead: ")
        music = pyglet.resource.media(file)
        music.play()
    
