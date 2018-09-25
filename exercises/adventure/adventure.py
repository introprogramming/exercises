import sys
from locations import *
from location import *
from switch import *

current_location = 'haunted forest'
here = locations[current_location]

def move(direction):
    global here, current_location
    new_loc = here.get_neighbor(direction)

    if (new_loc):
        current_location = new_loc
        here = locations[current_location]
    else:
        print ("No route leading " + direction + ".\n")

    look()

def look(direction=""):
    if (direction):
        target = here.get_neighbor(direction)
        if (target):
            view = locations[target].short_view()
        else:
            view = "There's nothing there."
        print (view)
    else:
        print (here.name)
        print (here.long_view())
        print ("")
        here.print_exits()
    

def perform_action(input):
    here.do_something(input)



def await_action():
    user_input = input("> ").split()

    for case in switch(user_input[0]):
        if case('quit'):
            print ("Bye!")
            return

        if case('go','move'):
            if len(user_input) > 1:
                move(user_input[1])
            else:
                print ("Where to?")
            break

        if case('look'):
            if len(user_input) > 1:
                look(user_input[1])
            else:
                look()
            break

        # We have a custom action
        perform_action(user_input)
    
    await_action()

"""
  This starts the adventure game loop.
"""

look()
await_action()
