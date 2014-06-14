
def print_scores(players, score):
    """Print the entire scoreboard and sum of points"""
    #There is probably a much better way of doing this
    
    name_string = "  "
    for player in players:
        name_string += "\t" + player
        score[player]['sum'] = 0
    print name_string
    
    for key in score_model.keys():
        string = key + ":"
        for player in players:
            if key in score[player]:
                part_score = score[player][key]
                string += "\t" + str(part_score)
            else:
                part_score = 0
                string += "\t-"
            
            score[player]['sum'] += part_score
        
        print string
    
    sum_string = "Sum:"
    for player in players:
        sum_string += "\t" + str(score[player]['sum'])

def number_points(n, dice):
    """Rule for ordinary number scores: ex all 5.
    Returns the `n` number score for these `dice`."""
    points = 0
    for ix in dice:
        if ix == n:
            points += ix
    if points/n > 2:
        print "Well done, you got " + str(points) + " points"
    else:
        print "Better luck next time, you got " + str(points) + " points"
    return points
    
score_model = {\
    '1': (lambda(d): number_points(1, d)),\
    '2': (lambda(d): number_points(2, d)),\
    '3': (lambda(d): number_points(3, d)),\
    '4': (lambda(d): number_points(4, d)),\
    '5': (lambda(d): number_points(5, d)),\
    '6': (lambda(d): number_points(6, d)),\
    'chans':sum}

def points_of(dice, player_score):
    """Decides which score to use and updates scoreboard.
    
    Is called at the end of each player turn. Each score can only be used once per player."""
    
    print "Your current scoreboard:"
    #Kind of a hack :P, wants to reuse code. Could print entire board but not really relevant.
    sub_board = {}
    sub_board[" "] = player_score
    print_scores(" ", sub_board)
    
    choice = '-1'
    while choice not in score_model.keys():
        print "Which score do you want to use?"
        
        
        choice = raw_input("\t").replace(" ", "")
        if choice in player_score:
            print "Already used " + choice
            choice = '-1'
            continue
    
    #Evaluate function pointer
    points = score_model[choice](dice)
    player_score[choice] = points

