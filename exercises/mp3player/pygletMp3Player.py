import pyglet
from pyglet.window import key

#Pyglet implementation

music = pyglet.resource.media('sample.wav')
music.play()

window = pyglet.window.Window()

paused = False

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.P:
        global paused
        if paused:
            player.play()
            paused = False
        else:
            player.pause()
            paused = True

pyglet.app.run()


print "SO FAR :)"
player = pyglet.media.Player()

def help():
    print """\nCommands:
\tend or exit \t Exit program
\tpl or play \t Play this file
\tp or pause \t Pause/unpause music
\tq or queue \t Add music to queue
\tn or next \t Skip to next piece
\tr or rewind \t Play from the start
\th or help \t See this list again"""

print """Welcome to this music player!

You can give a file as an argument or use the commands below."""
help()

# Listen for user input
print "LISTEN :)"
s=raw_input()
paused = False
while s!="end" and s!="exit":
    if s == "r" or s == "rewind":
        player.seek(0)
    
    elif s == "p" or s == "pause":
        if paused:
            player.play()
            paused = False
        else:
            player.pause()
            paused = True
    
    elif s == "q" or s == "queue":
        file = raw_input("Add file to queue: ")
        music = pyglet.resource.media(file)
        player.queue(music)
    elif s == "n" or s == "next":
        player.next()
    elif s == "pl" or s == "play":
        file = raw_input("Play this file instead: ")
        music = pyglet.resource.media(file)
        music.play()
    elif s == "h" or s == "help":
        help()
    elif s == "":
        pass
    else:
        print "I don't understand what you mean with '"+s+"'. Type `h` or `help` to see a list of commands."
    s=raw_input()

pyglet.app.exit()