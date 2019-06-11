gameArea = ['_'] * 9  # initialize a gamearea with nine underscore characters. Symbolising empty spot

playerOneSign = 'X'
playerTwoSign = 'O'

players = ["Player1", "Player2"]
signs = [playerOneSign, playerTwoSign]


def is_busy(position):  # determin if the position is occupied already or out of bounds
    if 0 <= position < 9:
        # not gameArea[position] == '_' works as well
        return gameArea[position] == playerOneSign or gameArea[position] == playerTwoSign
    return False


def is_sign_exist(sign, position):
    if 0 <= position < 9:
        return gameArea[position] == sign
    return False


def check_columns(sign):
    return check_direction(3, sign) or check_direction(3, sign, 1) or check_direction(3, sign, 2)


def check_rows(sign):
    return check_direction(1, sign, 0) or check_direction(1, sign, 3) or check_direction(1, sign, 6)


def check_direction(direction, sign, offset=0):
    if direction == 2:  # diagonal righUp to leftDown
        return is_sign_exist(sign, direction) and \
               is_sign_exist(sign, 2 * direction) and \
               is_sign_exist(sign, 3 * direction)
    elif direction == 3:  # columns
        return is_sign_exist(sign, 0 + offset) and \
               is_sign_exist(sign, direction + offset) and \
               is_sign_exist(sign, 2 * direction + offset)
    elif direction == 1:  # rows
        return is_sign_exist(sign, offset) and \
               is_sign_exist(sign, offset + 1) and \
               is_sign_exist(sign, offset + 2)
    elif direction == 4:  # second diagonal leftUp to rightDown
        return is_sign_exist(sign, 0) and \
               is_sign_exist(sign, direction) and \
               is_sign_exist(sign, 2 * direction)
    else:
        return False


def has_three_in_row(sign):
    return check_rows(sign) or check_direction(2, sign) or check_columns(sign) or check_direction(4, sign)


def place_sign(position, sign):
    position -= 1  # Compensating 0-indexed list so user can enter 1-9
    if not is_busy(position) and 0 <= position < 9:
        gameArea[position] = sign
        return True
    else:
        return False


def print_game_area():
    board_text = ""
    for num in range(0, 9):
        board_text += str(gameArea[num])
        if num % 3 == 2:
            board_text += "\n"
        else:
            board_text += " "
    print(board_text + "\n")
    return


def play():
    count = 0
    while True:
        print_game_area()
        print("{}'s turn".format(players[count % 2]))
        desired_pos = int(input("Please enter where you want to place your sign "))
        while True:  # simulating do-while loop
            if place_sign(desired_pos, signs[count % 2]):
                break
            desired_pos = int(input("Sorry, you can't place at that position. Choose another "))
        if has_three_in_row(signs[count % 2]):
            print("{} won".format(players[count % 2]))
            print_game_area()
            return
        if count >= 8:
            print("It's a tie")
            print_game_area()
            return
        count += 1


play()
