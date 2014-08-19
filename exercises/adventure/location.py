from switch import *

class LocationState:

    short_desc = ""
    long_desc  = ""

    directions = {}

    actions = {}

    def __init__(self, short, long, dirs, acts):
        self.short_desc = short
        self.long_desc  = long
        self.directions = dirs
        self.actions    = acts

class Location:

    name = "Alien Mothership"
    states = []
    current_state_ix = 0 
    current_state = ""

    # Args should be a non-empty set of LocationStates
    def __init__(self, name, *args):
        self.name = name
        self.states = args
        self.current_state = self.states[0]

    def short_view(self):
        return self.current_state.short_desc

    def long_view(self):
        return self.current_state.long_desc

    def get_neighbor(self, direction):
        possible_dirs = self.current_state.directions
        if (direction in possible_dirs):
            return possible_dirs[direction]
        else:
            return ""


    def print_exits(self):
        possible_dirs = self.current_state.directions.keys()
        
        for case in switch(len(possible_dirs)):
            if case(0):
                print "All dressed up and nowhere to go!"
                break
            if case(1):
                print "There's an exit " + possible_dirs[0]
                break
            else:
                print "There are exits ",
                print possible_dirs[0],
                for ex in possible_dirs[1:]:
                    print ", " + ex,
                print "."
        


    def do_something(self, input):
        possible_actions = self.current_state.actions
        if (input[0] in possible_actions):
            possible_actions[input[0]](input[1:])
        else:
            print "Interesting."

    def set_state(self, new_state):
        self.current_state_ix = new_state
        self.current_state = self.states[new_state]
