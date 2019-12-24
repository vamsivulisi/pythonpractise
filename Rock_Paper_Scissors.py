import random
def play_game():
    valid = True
    selection = input("selct you'r choice 'p' for 'paper' 's' for 'scissors' and 'r' for 'rock':")
    while valid:
        if str(selection) == "p":
            selection = "Paper"
            valid = False
        elif str(selection) == "s":
            selection = "Scissors"
            valid = False
        elif str(selection) == "r":
            selection = "Rock"
            valid = False
        else:
            selection = input(
                " Enter valid letter selct you'r choice 'p' for 'paper' 's' for 'scissors' and 'r' for 'rock':")
    print("player: " +selection)
    c_i = random.randint(1, 3)
    if str(c_i) == "1":
        c_i = "Paper"
    elif str(c_i) == "2":
        c_i = "Scissors"
    elif str(c_i) == "3":
        c_i = "Rock"
    print("system: " + c_i)
    f = True
    while f:
        if selection == "Paper":
            if c_i == "Rock":
                print("you won")
                f = False
            elif c_i == "Scissors":
                print("you loose")
                f = False
            elif c_i == "Paper":
                print ("tie")
                return
        elif selection == "Rock":
            if c_i == "Scissors":
                print("you won")
                f = False
            elif c_i == "Paper":
                print("you loose")
                f = False
            elif c_i == "Rock":
                print ("tie")
                return
        elif selection == "Scissors":
            if c_i == "Paper":
                print("you won")
                f = False
            elif c_i == "Rock":
                print("you loose")
                f = False
            elif c_i == "Scissors":
                print ("tie")
                return

play_game()
