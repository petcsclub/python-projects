board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

player_X = "X"
player_O = "O"
current_player = player_X


def print_board():
    """Print out the board."""

    # prints out the indexes of each column
    print("\n  0   1   2")

    # prints out the values of the first row of the board
    print(f"0 {board[0][0]} | {board[0][1]} | {board[0][2]}")

    # prints out a line to seperate rows 
    print(" ---+---+---")
    
    # prints out the values of the second row of the board
    print(f"1 {board[1][0]} | {board[1][1]} | {board[1][2]}")

    # prints out a line to seperate rows 
    print(" ---+---+---")    

    # prints out the values of the third row of the board
    print(f"2 {board[2][0]} | {board[2][1]} | {board[2][2]}")


def all_same(list):
    """Take in a list, return whether all its elements are the same."""
    for item in list:
        if item != list[0] or item == " ":
            return False

    return True


def win():
    """Return whether someone has won."""

    # checks horizontally
    for row in board:
        if all_same(row):
            return True

    # checks vertically
    for column in range(3):
        check = []
        for row in board:
            check.append(row[column])
        if all_same(check):
            return True

    # checks diagonally (\)
    if all_same([board[0][0], board[1][1], board[2][2]]):
        return True

    # checks diagonally (/)
    if all_same([board[2][0], board[1][1], board[0][2]]):
        return True

    return False


def tie():
    """Return whether the game is a tie"""
    for row in board:
        for space in row:
            if space == " ":
                return False

    return True


# main game loop
playing = True
while playing:
    # displays board
    print_board()

    # displays whose turn it is
    print(f"\n{current_player}'s turn!")

    # asks player where to place their mark, 
    # if choice is occupied, doesn't exist, or causes an error, it repeats
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

    # if someone wins or there's a tie, displays the winner and ends the main game loop
    # if not, gives turn to next player and repeats main game loop
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