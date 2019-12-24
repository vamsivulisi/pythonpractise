#tic-toc
#board
#display_board
#TURN_PLAYERS
#check_gameover
#play_game


Board = ['-','-','-',
         '-','-','-',
         '-','-','-']
winner = None
game_still_going = True
current_player = "x"
def Display_board():
    print(Board[0] + " | " + Board [1] +  " | "  + Board[2])
    print(Board[3] + " | " + Board[4] + " | " + Board[5])
    print(Board[6] + " | " + Board[7] + " | " + Board[8])

def turn_players ():
    global current_player
    if current_player == "x":
        print ("player A's turn")
    elif current_player == "o":
        print ("player B's turn")
    position = input ( "select a position from 1-9: ")
    valid = False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input ("emayya memu em cheppam nv em chestunnav, select a position from 1-9:")
        position = int(position)-1
        if Board[position] == '-':
            valid = True
        else:
            print("don't cheat")
    Board[position] = current_player
    Display_board()
def check_row():
    global game_still_going
    row1 = Board[0] == Board[1] == Board[2] !='-'
    row2 = Board[3] == Board[4] == Board[5] !='-'
    row3 = Board[6] == Board[7] == Board[8] !='-'
    if row1 or row2 or row3 :
        game_still_going = False
    if row1:
        return Board[0]
    elif row2:
        return Board[3]
    elif row3:
        return Board[6]
    return
def check_column():
    global game_still_going
    column1 = Board[0] == Board[3] == Board[6] !='-'
    column2 = Board[1] == Board[4] == Board[7] !='-'
    column3 = Board[2] == Board[5] == Board[8] !='-'
    if column1 or column2 or column3:
        game_still_going = False
    if column1:
        return Board[0]
    elif column2:
        return Board[1]
    elif column3:
        return Board[2]
    return
def check_diagonal():
    global game_still_going
    diagonal1 = Board[0] == Board[4] == Board[8] !='-'
    diagonal2 = Board[2] == Board[4] == Board[6] !='-'
    if diagonal1 or diagonal2:
        game_still_going = False
    if diagonal1:
        return Board[0]
    elif diagonal2:
        return Board[2]
    return
def check_winner ():
    global winner
    row_winner = check_row()
    column_winner = check_column()
    diagonal_winner = check_diagonal()
    if row_winner :
        winner = row_winner
    elif column_winner :
        winner = column_winner
    elif diagonal_winner:
        winner =  diagonal_winner
    else:
        winner = None
    return

def check_if_tie():
    global game_still_going
    if "-" not in Board:
        game_still_going = False
    return
def check_if_gameover():
    check_winner()
    check_if_tie()

def flip_player():
    global current_player
    if current_player == "x":
        current_player= "o"
    elif current_player == "o":
        current_player = "x"
    return
def play_game():
    Display_board()
    while game_still_going:
        turn_players()
        check_if_gameover()
        flip_player()
    if winner =="x":
        print ("player A won")
    elif winner == "o":
        print ("player B won")
    else:
        print("Tie")

play_game()