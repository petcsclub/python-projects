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

    switch_player()