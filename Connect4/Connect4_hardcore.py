# Additions in hardcore mode:
# Customizable board size
# Option to play new game
# Win counter
# Change number of circles in a row needed to win

board_rows = 7
board_columns = 6
board = []

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

players = ["r", "y"]
current_player = players[0]


# displays board
def print_board():
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


# gets the bottommost empty space in a column
def bottom_row(column):
    for row in reversed(range(len(board))):
        if board[row][column] == " " and column >= 0:
            return row

    return None


# switches player
def switch_player():
    global current_player
    if current_player == players[0]:
        current_player = players[1]
    else:
        current_player = players[0]


# checks if all elements in a list are the same
def all_same(list):
    for item in list:
        if item != list[0] or item == " ":
            return False

    return True


# checks if someone wins
def win():
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


# checks if the game is a tie
def tie():
    for row in board:
        for space in row:
            if space == " ":
                return False

    return True


# main game loop
playing = True
while playing:
    # asks player what board size they want
    # if rows/columns is less than 1 or causes an error, it repeats
    board = []
    getting_board_size = True
    while getting_board_size:
        try:
            board_rows = int(input("How many board rows? "))
            board_columns = int(input("How many board columns? "))

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
            game_ongoing = False
        elif tie():
            print_board()
            print(f"\nTie!")
            game_ongoing = False
        else:
            switch_player()

    # asks player if they want to play another game
    # if yes, repeats the main game loop
    # if no, ends main game loop
    getting_again_choice = True
    while getting_again_choice:
        again_choice = input("Play another game? (y/n) ")
        if again_choice == "y":
            print("Generating another game!\n")
            getting_again_choice = False
        elif again_choice == "n":
            print("Aight, peace")
            getting_again_choice = False
            playing = False
        else:
            print("Invalid choice!")