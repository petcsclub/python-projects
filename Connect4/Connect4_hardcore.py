# Additions in hardcore mode:
# Customizable board size
# Option to play new game
# Win counter

board_columns = 7
board_rows = 6
board = []
players = ["r", "y"]
current_player = players[0]
symbols = {
    "r": "🔴 ",
    "y": "🟡 ",
    " ": "⚪ ",
    0: "0️⃣  ",
    1: "1️⃣  ",
    2: "2️⃣  ",
    3: "3️⃣  ",
    4: "4️⃣  ",
    5: "5️⃣  ",
    6: "6️⃣  ",
    7: "7️⃣  ",
    8: "8️⃣  ",
    9: "9️⃣  ",
}
wins = {
    "r": 0,
    "y": 0
}


def print_board():
    """Print out the board."""

    # adds newline before displaying the board
    print()

    # the below code prints out each digit of the column indexes in a seperate line,
    # so if a board size wider than 10 is chosen, 
    # the indexes don't offset due to them having multiple digits

    # repeats for each digit in the largest board column index
    for digit in range(len(str(len(board[0])))):
        # creates string that will display the specific digit of each index
        column_indexes_print = ""

        # repeats for each board column
        for column_index in range(len(board[0])):

            # pads the column index to be the same length as the largest index
            # so if the index doesn't have a tens digit for example, it won't print anything
            padded_column_index = str(column_index).rjust(len(str(len(board[0]))), "n")
            
            # check if the index has the specific digit
            # if yes, add the digit (converted to emoji form) to column_indexes_print
            # if no, adds an empty space to column_indexes_print
            if padded_column_index[digit].isdigit():
                column_indexes_print += symbols[int(padded_column_index[digit])]
            else:
                column_indexes_print += "  "

        # print out the specific digit of each column index
        print(column_indexes_print)

    # repeats for each row in the board
    for row in range(len(board)):
        # creates string that will represent the values in the row
        row_print = ""

        # adds each value in the row to row_print
        for space in board[row]:
            row_print += symbols[space]

        # prints the values in the row
        print(row_print)


def bottom_row(column):
    """Return the bottommost empty space in a column."""
    for row in reversed(range(len(board))):
        if board[row][column] == " " and column >= 0:
            return row

    return None


def switch_player():
    """Switch the current player"""
    global current_player
    if current_player == players[0]:
        current_player = players[1]
    else:
        current_player = players[0]


def all_same(l):
    """Take in a list, return whether all its elements are the same."""
    return l.count("r") == 4 or l.count("y") == 4


def win():
    """Return whether someone has won."""

    # checks horizontally
    for row in range(len(board)):
        for column in range(len(board[row]) - 3):
            if all_same([
                board[row][column], 
                board[row][column + 1],
                board[row][column + 2],
                board[row][column + 3]
            ]):
                return True

    # checks vertically
    for row in range(len(board) - 3):
        for column in range(len(board[row])):
            if all_same([
                board[row][column],
                board[row + 1][column],
                board[row + 2][column],
                board[row + 3][column]
            ]):
                return True

    # checks diagonally (\)
    for row in range(len(board) - 3):
        for column in range(len(board[row]) - 3):
            if all_same([
                board[row][column],
                board[row + 1][column + 1],
                board[row + 2][column + 2],
                board[row + 3][column + 3]
            ]):
                return True

    # checks diagonally (/)
    for row in range(3, len(board)):
        for column in range(len(board[row]) - 3):
            if all_same([
                board[row][column],
                board[row - 1][column + 1],
                board[row - 2][column + 2],
                board[row - 3][column + 3]
            ]):
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
    board = []
    getting_board_size = True

    # asks player if they want to have a custom board size
    # if answer isn't y or n, it repeats
    while True:
            resize_choice = input("Change board size? (y/n) ").lower()

            if resize_choice == "y":
                getting_board_size = True
                break
            elif resize_choice  == "n":
                getting_board_size = False
                break
            else:
                print("Invalid choice!")

    # asks player what board size they want
    # if rows/columns is less than 1 or causes an error, it repeats
    if getting_board_size:
        while True:
            board_column_choice = input("How many board columns? ")
            board_row_choice = input("How many board rows? ")

            if (
                board_column_choice.isdigit() and
                board_row_choice.isdigit() and
                int(board_column_choice) > 0 and 
                int(board_row_choice) > 0
            ):
                board_columns = int(board_column_choice)
                board_rows = int(board_row_choice)
                break
            else:
                print("Invalid choice!")

    # sets board size to equal to chosen length and width
    for row_size in range(board_rows):
        row = []
        for column_size in range(board_columns):
            row.append(" ")
        board.append(row)

    current_player = players[0]

    # loop that repeats while game is ongoing
    while True:
        # displays board
        print_board()

        # displays whose turn it is
        print(f"\n{symbols[current_player]}'s turn!")

        # asks player which column to place their circle, 
        # if column is occupied, doesn't exist, or causes an error, it repeats
        while True:
            column = input("Which column? ")
            if (
                column.isdigit() and
                int(column) < len(board[0]) and
                board[bottom_row(int(column))][int(column)] == " "
            ):
                board[bottom_row(int(column))][int(column)] = current_player
                break
            else:
                print("Invalid choice!")

        # if someone wins or there's a tie, displays the winner and ends the main game loop
        # if not, gives turn to next player and repeats main game loop
        if win():
            print_board()
            print(f"\n{symbols[current_player]} wins!")
            wins[current_player] += 1
            break
        elif tie():
            print_board()
            print(f"\nTie!")
            break
        else:
            switch_player()

    # displays the win counter for each player
    print(f"\n{symbols[players[0]]}'s wins: {wins[players[0]]}")
    print(f"{symbols[players[1]]}'s wins: {wins[players[1]]}")

    # asks player if they want to play another game
    # if yes, repeats the main game loop
    # if no, ends main game loop
    while True:
        again_choice = input("Play another game? (y/n) ").lower()
        if again_choice == "y":
            print("Generating another game!\n")
            break
        elif again_choice == "n":
            print("Aight, peace ✌")
            playing = False
            break
        else:
            print("Invalid choice!")