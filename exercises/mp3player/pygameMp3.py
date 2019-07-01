import pygame, sys
#import time

file = "sample.wav"
if len(sys.argv)>1:
    file = sys.argv[1]

pygame.mixer.init(44100) #Set sample rate
pygame.mixer.music.load(file)
pygame.mixer.music.play(0)

def help():
    print("""\nCommands:
\tend or exit \t Exit program
\tr or rewind \t Play from the start
\tp or pause \t Pause/unpause music
\ts or stop \t Stop playing this one
\tpl or play \t Play this file
\th or help \t See this list again""")
#\tq or queue \t Add music to queue


print("""Welcome to this music player!

You can give a file as an argument or use the commands below.""")
help()

# Listen for user input
s=input()
paused = False
while s!="end" and s!="exit":
    if s == "r" or s == "rewind":
        #pygame.mixer.music.rewind()
        pygame.mixer.music.play(0)
    elif s == "p" or s == "pause":
        if paused:
            pygame.mixer.music.unpause()
            paused = False
        else:
            pygame.mixer.music.pause()
            paused = True

    # Queue function seems to be defect :P
    #elif s == "q" or s == "queue":
    #    file = raw_input("Add file to queue: ")
    #    pygame.mixer.music.queue(file)
    elif s == "s" or s == "stop":
        pygame.mixer.music.stop()
    elif s == "pl" or s == "play":
        file = input("Play this file instead: ")
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(0)
    elif s == "h" or s == "help":
        help()
    elif s == "":
        pass
    else:
        print("I don't understand what you mean with '"+s+"'. Type `h` or `help` to see a list of commands.")
    s=input()