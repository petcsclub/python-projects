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
    "r": "🔴",
    "y": "🟡",
    " ": "⚪",
    0: "0️⃣ ",
    1: "1️⃣ ",
    2: "2️⃣ ",
    3: "3️⃣ ",
    4: "4️⃣ ",
    5: "5️⃣ ",
    6: "6️⃣ ",
    7: "7️⃣ ",
    8: "8️⃣ ",
    9: "9️⃣ ",
}
wins = {
    "r": 0,
    "y": 0
}


def print_board():
    """Print out the board."""
    print()
    for digit in range(len(str(len(board[0])))):
        column_indexes_print = ""
        for column_index in range(len(board[0])):
            padded_column_index = str(column_index).rjust(len(str(len(board[0]))), "n")
            try:
                column_indexes_print += symbols[int(padded_column_index[digit])]
            except:
                column_indexes_print += "  "
        print(column_indexes_print)

    for row in range(len(board)):
        row_print = ""
        for space in board[row]:
            row_print += symbols[space]
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


def all_same(list):
    """Take in a list, return whether all its elements are the same."""
    for item in list:
        if item != list[0] or item == " ":
            return False

    return True


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

    # asks player if they want to have a custom board size
    # if answer isn't y or n, it repeats
    getting_board_size = True
    getting_resize_choice = True
    while getting_resize_choice:
        try:
            resize_choice = input("Change board size? (y/n) ").lower()

            if resize_choice == "y":
                getting_board_size = True
                getting_resize_choice = False
            elif resize_choice  == "n":
                getting_board_size = False
                getting_resize_choice = False
            else:
                raise Exception()
        except:
            print("Invalid choice!")

    # asks player what board size they want
    # if rows/columns is less than 1 or causes an error, it repeats
    while getting_board_size:
        try:
            board_columns = int(input("How many board columns? "))
            board_rows = int(input("How many board rows? "))

            if board_rows <= 0 or board_columns <= 0:
                raise Exception()
            else:
                getting_board_size = False
        except:
            print("Invalid choice!")

    # sets board size to equal to chosen length and width
    for row_size in range(board_rows):
        row = []
        for column_size in range(board_columns):
            row.append(" ")
        board.append(row)

    current_player = players[0]

    # loop that repeats while game is ongoing
    game_ongoing = True
    while game_ongoing:
        # displays board
        print_board()

        # displays whose turn it is
        print(f"\n{symbols[current_player]}'s turn!")

        # asks player which column to place their circle, 
        # if column is occupied, doesn't exist, or causes an error, it repeats
        played = False
        while not played:
            try:
                column = int(input("Which column? "))

                board[bottom_row(column)][column] = current_player
                played = True
            except:
                print("Invalid choice!")

        # if someone wins or there's a tie, displays the winner and ends the main game loop
        # if not, gives turn to next player and repeats main game loop
        if win():
            print_board()
            print(f"\n{symbols[current_player]} wins!")
            wins[current_player] += 1
            game_ongoing = False
        elif tie():
            print_board()
            print(f"\nTie!")
            game_ongoing = False
        else:
            switch_player()

    # displays the win counter for each player
    print(f"\n{symbols[players[0]]}'s wins: {wins[players[0]]}")
    print(f"{symbols[players[1]]}'s wins: {wins[players[1]]}")

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