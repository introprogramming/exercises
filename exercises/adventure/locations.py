import sys
from location import *
from switch import *

"""
The haunted forest
"""
def __haunted_forest_pick(input):
    if input:
        for case in switch(input[0]):
            if case('mushroom', 'mushrooms'):
                if haunted_forest.current_state_ix == 0:
                    print "Mmm... Mushrooms!\n"
                    haunted_forest.set_state(1)
                else:
                    print "Where have all the mushrooms gone? Young girls picked them everyone!"
                break
            if case('tree','trees'):
                print "You're not that strong, silly!"
                break
            if case('stuff'):
                print "Some stuff stuffed away."
                break
            else:
                print "Ain't no " + input[0] + " around here"
    else:
        print "Pick-pickety-pick... pickaxe?"

def __haunted_forest_sing(input):
    if input:
        for case in switch(input[0]):
            if case('halelujah'):
                print "The world has become a brighter place!"
                haunted_forest.set_state(2)
                break
            else:
                print "*sings* " + input[1]
    else:
                print "I'm siiiiiiingin' in the rain!"
        

haunted_forest = Location('The Haunted Forest', 
    LocationState(
        "A dark and dreary place.",
        "A scary forest full of trees and mushrooms and stuff.",
        {}, 
        {'pick': __haunted_forest_pick}
    ),
    LocationState(
        "A dark and dreary place.",
        "A scary forest full of trees but no mushrooms.",
        {},
        {'pick': __haunted_forest_pick,
         'sing': __haunted_forest_sing}
    ),
    LocationState(
        "A dark and dreary place.",
        "A scary forest full of trees but no mushrooms.",
        {'west':'shining plains'},
        {'pick': __haunted_forest_pick,
         'sing': __haunted_forest_sing}
    )
)

"""
  The Shining Plains.
"""

def __shining_plains_win(input):
    print "Awesome! You have won the game!"
    sys.exit()

shining_plains = Location('The Shining Plains',
     LocationState(
         "A bright and beautiful place.",
         "A really bright and beautiful plains with daffodils and dandelions.",
         {'east':'haunted forest'},
         {'win': __shining_plains_win}
     ))

#####################################################3

""" Make the locations easily indexable"""
locations = {
    'haunted forest': haunted_forest,
    'shining plains': shining_plains
}

