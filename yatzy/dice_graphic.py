

dice_graph = {}
dice_graph['1_top'] = {}
dice_graph['2_mid'] = {}
dice_graph['3_bot'] = {}

dice_graph['1_top']['1'] = "|     |"
dice_graph['2_mid']['1'] = "|  o  |"
dice_graph['3_bot']['1'] = "|     |"

dice_graph['1_top']['2'] = "|o    |"
dice_graph['2_mid']['2'] = "|     |"
dice_graph['3_bot']['2'] = "|    o|"

dice_graph['1_top']['3'] = "|o    |"
dice_graph['2_mid']['3'] = "|  o  |"
dice_graph['3_bot']['3'] = "|    o|"

dice_graph['1_top']['4'] = "|o   o|"
dice_graph['2_mid']['4'] = "|     |"
dice_graph['3_bot']['4'] = "|o   o|"

dice_graph['1_top']['5'] = "|o   o|"
dice_graph['2_mid']['5'] = "|  o  |"
dice_graph['3_bot']['5'] = "|o   o|"

dice_graph['1_top']['6'] = "|o   o|"
dice_graph['2_mid']['6'] = "|o   o|"
dice_graph['3_bot']['6'] = "|o   o|"

def print_d(n):
    print dice_graph['1_top'][n]
    print dice_graph['2_mid'][n]
    print dice_graph['3_bot'][n]

def print_dice(list):
    spacing = "  "
    
    string = ""
    for ix in list:
        string += " _____ " + spacing
    print string
    
    for key in dice_graph.values():
        #print key
        string = ""
        for ix in list:
            string += key[str(ix)] + spacing
        print string
    
#print_dice([1, 1, 5, 4, 1])
