board = [[" ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " "]]

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
    column_indexes_print = "\n"
    for column_index in range(len(board[0])):
        column_indexes_print += symbols[column_index]
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
        playing = False
    elif tie():
        print_board()
        print(f"\nTie!")
        playing = False
    else:
        switch_player()