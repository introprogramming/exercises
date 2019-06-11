
import sys, random

players = ["", ""]

#AI difficulty
# 0 means totally random AI
# 1 means 50% chance of poor decision
# 3 means 25% chance of poor decision etc
ai_difficulty = 3

def read_name(ix):
    """Reads player name from CLI, returns string."""
    return input( "What is your name (Player" + str(ix) + ")?\n\t")

def start(multiplayer):
    """Sets player names by input or AI, depending on multiplayer or not."""
    players[0] = read_name(1)
    if(multiplayer):
        players[1] = read_name(2)
    else:
        players[1] = "AI"

def print_sticks(sticks):
    """Prints a graphical representation of the sticks left.
    Prints one space per 5 sticks."""
    ix = 1
    string = "\n"
    while ix <= sticks:
        string += "|"
        if (ix%5 == 0):
            string += " "
        ix = ix + 1
    print(string)

def play_turn(player_name, sticks):
    """Returns 1 or 2,
    depending on player's choice."""
    choice = -1
    while choice != 1 and choice != 2:
        print_sticks(sticks)
        choice = int(input(player_name + ": pick 1 or 2 sticks?\n\t"))
        if choice !=1 and choice != 2:
            print("Can only pick 1 or 2, not "+str(choice))
        
    return choice

def ai_turn(sticks):
    """Returns 1 or 2, 
    depending on the somewhat intelligent choice of AI."""
    print_sticks(sticks)
    
    #Smart strategy:
    choice = sticks%3
    
    #When strategy fails or chance says it's time for a random decision
    if choice == 0 or random.randint(0,ai_difficulty) == 0:
        choice = random.randint(1,2)
    
    # No AI should be so stupid as to pick one when there are only two left.
    if sticks < 3:
        choice = sticks
    
    string = "AI picks " + str(choice) + " stick"
    if(choice > 1 ):
        string += "s."
    else:
        string += "."
    print(string)
    return choice

def game():
    """Starts a new game of Pick one pick two.
    Makes a 1vsAI game if argument is 'ai', otherwise 1v1."""
    
    print("Game: Pick one pick two!\n")
    print("\n-------------------------")
    
    multiplayer = True
    if len(sys.argv) > 1 and sys.argv[1]=="ai":
        multiplayer = False
    
    start(multiplayer)
    
    sticks = random.randint(15, 25)
    turn = 1
    #last_player = ""
    while sticks > 0:
        last_player = players[turn % len(players)]
        if(not multiplayer and last_player == "AI" ):
            sticks -= ai_turn(sticks)
        else:
            sticks -= play_turn( last_player, sticks )
        turn = turn + 1
    
    print("\n-------------------------")
    print(last_player + " won!")

# Main
game()