# Additions in hardcore mode:
# Customizable board size
# Option to play new game
# Win counter

board_size = 3
board = []

player_X = "X"
player_O = "O"
current_player = player_X
playing = True
wins = {
    player_X: 0,
    player_O: 0
}


def print_board():
    """Print out the board."""

    # adds the index of each board column to a string, and prints it
    column_indexes_print = "\n  "
    for column_index in range(len(board[0])):
        column_indexes_print += f"{column_index}   "
    print(column_indexes_print)

    # repeats for each row in the board
    for row_index in range(len(board)):
        # creates a string that will represent the row that starts with the row's index
        row_print = f"{row_index}"

        # adds each value in the row to row_print
        for column_index in range(len(board[row_index])):
            row_print += f" {board[row_index][column_index]} "

            # unless the last value in the row is reached, add a "|" to seperate the values
            if column_index != len(board[row_index]) - 1:
                row_print += "|"

        # prints out the row
        print(row_print)

        # unless the last row is reached, creates a border to seperate the rows
        if row_index != len(board) - 1:

            # creates a string that will represent the border
            row_border_print = " "

            # repeats for each value in the row
            for column_index in range(len(board[row_index])):
                # add "---" to the string
                row_border_print += "---"

                # unless the last value is reached, add "+" to the string.
                # these give the illusion of the "|" and "---" intersecting
                if column_index != len(board[row_index]) - 1:
                    row_border_print += "+"

            # prints out the row border
            print(row_border_print)


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
    for column in range(len(board[0])):
        check = []
        for row in board:
            check.append(row[column])
        if all_same(check):
            return True

    # checks diagonally (\)
    check = []
    for index in range(len(board)):
        check.append(board[index][index])
    if all_same(check):
        return True

    # checks diagonally (/)
    check = []
    for index in range(len(board)):
        check.append(board[index][len(board) - index - 1])
    if all_same(check):
        return True

    return False


def tie():
    """Return whether the game is a tie"""
    for row in board:
        for spot in row:
            if spot == " ":
                return False

    return True

# main game loop
playing = True
while playing:
    # asks player what board size they want
    # if choice is less than 1 or causes an error, it repeats
    board = []
    getting_board_size = True
    while getting_board_size:
        try:
            board_size = int(input("What board size? (1-10) "))

            if board_size <= 0 or board_size > 10:
                raise Exception()
            else:
                getting_board_size = False
        except:
            print("Invalid choice!")

    # sets the board's number of rows and columns equal to the chosen board size
    for row_size in range(board_size):
        row = []
        for column_size in range(board_size):
            row.append(" ")
        board.append(row)

    current_player = player_X

    # loop that repeats while game is ongoing
    game_ongoing = True
    while game_ongoing:
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

        # checks if someone wins or there's a tie
        # if so, displays the winner, increments their win count, and ends ongoing game loop
        # if not, gives turn to next player and repeats ongoing game loop
        if win():
            print_board()
            print(f"\n{current_player} wins!")
            wins[current_player] += 1
            game_ongoing = False
        elif tie():
            print_board()
            print(f"\nTie!")
            game_ongoing = False
        else:
            if current_player == player_X:
                current_player = player_O
            else:
                current_player = player_X 

    # displays the win counter for each player
    print(f"X's wins: {wins[player_X]}")
    print(f"O's wins: {wins[player_O]}")

    # asks player if they want to play another game
    # if yes, repeats the main game loop
    # if no, ends main game loop
    getting_again_choice = True
    while getting_again_choice:
        again_choice = input("Play another game? (y/n) ").lower()
        if again_choice == "y":
            print("Generating another game!\n")
            getting_again_choice = False
        elif again_choice == "n":
            print("Aight, peace ✌")
            getting_again_choice = False
            playing = False
        else:
            print("Invalid choice!")