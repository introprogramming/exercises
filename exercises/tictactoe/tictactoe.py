gameArea = ['_'] * 9 #initialize a gamearea with nine underscore characters. Symbolising empty spot

playerOneSign = 'X'
playerTwoSign = 'O'

players = ["Player1", "Player2"]
signs = [playerOneSign, playerTwoSign]

def isBusy(position): #determin if the position is occupied already or out of bounds
    if(0 <= position and position < 9):
        #not gameArea[position] == '_' works as well
        return gameArea[position] == playerOneSign or gameArea[position] ==  playerTwoSign 
    return False

def isSignExist(sign, position):
    if 0 <= position and position < 9:
        return gameArea[position] == sign
    return False

def checkColumns(sign):
       return checkDirection(3, sign) or checkDirection(3, sign, 1) or checkDirection(3, sign, 2)

def checkRows(sign):
     return checkDirection(1, sign, 0) or checkDirection(1, sign, 3) or checkDirection(1, sign, 6)

def checkDirection(dir, sign, offset = 0):
    if(dir == 2):#diagonal righUp to leftDown
        return isSignExist(sign,dir) and isSignExist(sign, 2*dir) and isSignExist(sign,3*dir)
    elif(dir == 3): #columns
        return isSignExist(sign,0+offset) and isSignExist(sign, dir+offset) and isSignExist(sign, 2*dir+offset)
    elif(dir == 1): #rows
         return isSignExist(sign,offset) and isSignExist(sign, offset+1) and isSignExist(sign, offset+2)
    elif(dir == 4):# second diagonal leftUp to rightDown
         return isSignExist(sign,0) and isSignExist(sign, dir) and isSignExist(sign, 2*dir)
    else:
        return False

def hasThreeInRow(sign):
    return checkRows(sign) or checkDirection(2, sign) or checkColumns(sign) or checkDirection(4, sign)

def placeSign(position, sign):
    position -= 1 #Compensating 0-indexed list so user can enter 1-9
    if not isBusy(position) and  0 <= position and position < 9:
        gameArea[position] = sign
        return True
    else:
        return False


def printGameArea():

    for num in range(0,9):
        if (num % 3 == 2):
            print(gameArea[num] + "\n"),
        else:
            print(gameArea[num] + " "),
    print("\n")
    return

def play():
    count = 0
    while True:
        print("%s's turn") % players[count%2]
        desiredPos = int(raw_input("Please enter where you want to place your sign "))
        while True: #simulating do-while loop
                if(placeSign(desiredPos, signs[count%2])):
                    break
                desiredPos = int(raw_input("Sorry, you can't place at that position. Choose another "))
        if(hasThreeInRow(signs[count%2])):
            print "%s won" % players[count%2]
            printGameArea()
            return
        if(count >= 8):
            print "It's a tie"
            printGameArea()
            return
        printGameArea()
        count += 1

play()