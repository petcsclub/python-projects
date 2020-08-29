board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

player_X = "X"
player_O = "O"
current_player = player_X

def print_board():
    print("\n  0   1   2")
    print(f"0 {board[0][0]} | {board[0][1]} | {board[0][2]}")
    print(" ---+---+---")
    print(f"1 {board[1][0]} | {board[1][1]} | {board[1][2]}")
    print(" ---+---+---")    
    print(f"2 {board[2][0]} | {board[2][1]} | {board[2][2]}")

def all_same(list):
    for item in list:
        if item != list[0] or item == " ":
            return False

    return True

def win():
    for row in board:
        if all_same(row):
            return True

    for column in range(3):
        check = []
        for row in board:
            check.append(row[column])
        if all_same(check):
            return True

    if all_same([board[0][0], board[1][1], board[2][2]]):
        return True

    if all_same([board[2][0], board[1][1], board[0][2]]):
        return True

    return False

def tie():
    for row in board:
        for spot in row:
            if spot == " ":
                return False

    return True

playing = True
while playing:
    print_board()

    print(f"\n{current_player}'s turn!")

    played = False
    while not played:
        try:
            column = int(input("Which column? "))
            row = int(input("Which row? "))

            if board[row][column] == " ":
                board[row][column] = current_player
                played = True
            else:
                raise Exception()
        except:
            print("Invalid choice!")

    if win():
        print_board()
        print(f"\n{current_player} wins!")
        playing = False
    elif tie():
        print_board()
        print(f"\nTie!")
        playing = False
    else:
        if current_player == player_X:
            current_player = player_O
        else:
            current_player = player_X