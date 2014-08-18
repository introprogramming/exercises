import pyglet

music = pyglet.resource.media('button-09.wav')
music.play()

pyglet.app.run()
player = pyglet.media.Player()

def help():
    print """\nCommands:
\tend or exit \t Exit program
\tr or rewind \t Play from the start
\tp or pause \t Pause/unpause music
\ts or stop \t Stop playing this one
\tpl or play \t Play this file
\th or help \t See this list again"""
#\tq or queue \t Add music to queue

print """Welcome to this music player!

You can give a file as an argument or use the commands below."""
help()

# Listen for user input
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
        player.queue(file)
    elif s == "s" or s == "stop":
        pass
    elif s == "pl" or s == "play":
        pass
    elif s == "h" or s == "help":
        help()
    elif s == "":
        pass
    else:
        print "I don't understand what you mean with '"+s+"'. Type `h` or `help` to see a list of commands."
    s=raw_input()