
import sys, random, dice_graphic, scores

#Note - this implementation is not optimal at all but demonstrates how it could be done. Feel free to suggest improvements or alternative implementations.

#arguments: yatzy.py <num_players=2> <num_turns=6>

TOTAL_DICE = 5

def read_name(ix):
    """Reads player name from CLI, returns string."""
    return raw_input( "What is your name (Player" + str(ix) + ")?\n\t")

def start(players, score):
    """Read player names from CLI. Initiate dictionary for each player"""
    ix = 0
    while ix < len(players):
        players[ix] = read_name(ix+1)
        score[players[ix]] = {}
        ix = ix+1

def throw_dice(n):
    """Throw `n` dice, returns list of integers"""
    results = []
    while n > 0:
        results += [random.randint(1,6)]
        n = n-1
    return results

def string_to_digit_list(string):
    """Return list of integers
    
    Converts a string of integer characters to a list of integers, ignoring spaces:
    '1 23 4' -> [1,2,3,4]
    """
    return map(int, list(string.replace(" ", "")))

def play_turn(player_name, score):
    """A player's turn:
        1. Throw dice
        2. Choose which dice to keep and which to throw anew
        3. Count points
    """
    print "\n-------------------------"
    print "Player "+player_name
    
    used = ""
    for entry in score[player_name]:
        used += " " + str(entry)
    print "You have already used:" + used
    
    t = 3
    dice_to_throw = TOTAL_DICE
    kept = []
    dice = []
    while t > 0:
        t = t-1
        dice = kept + throw_dice(dice_to_throw)
        dice_graphic.print_dice(dice)
        
        # No more choices
        if t == 0:
            continue
        
        keep = string_to_digit_list(raw_input("Which dice do you want to keep? (Can keep any or all, type numbers)\n\t"))
        
        check = {}
        for ix in keep:
            if str(ix) in check:
                #attempt cheating
                print "Cannot pick the same dice more than once! "
                print str(ix) + " has already been picked."
                continue
                
            check[str(ix)] = 0
            kept += [dice[ix-1]]
        dice_to_throw = TOTAL_DICE - len(kept)
        
        if dice_to_throw <= 0:
            break
    
    print "Finally:"
    dice_graphic.print_dice(dice)
    scores.points_of(dice, score[player_name])




def game():
    """Starts a new game of Yatzy"""
    print "Game: Yatzy!\n"
    print "\n-------------------------"
    
    num_players = 2
    if len(sys.argv) > 1:
        num_players = int(sys.argv[1])
    
    turn = 6
    if len(sys.argv) > 2:
        turn = int(sys.argv[2])
    
    players = [""]*num_players
    
    scoreboard = {}
    start(players, scoreboard)
    
    while turn > 0:
        for player in players:
            play_turn(player, scoreboard)
        turn = turn - 1
    
    print "\n-------------------------"
    scores.print_scores(players, scoreboard)

# Main
game()