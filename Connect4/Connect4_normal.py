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
    col_indexes_print = "\n"
    for col_index in range(len(board[0])):
        col_indexes_print += f"{symbols[col_index]}"
    print(f"{col_indexes_print}")

    for row in range(len(board)):
        row_print = ""
        for space in board[row]:
            row_print += symbols[space]
        print(f"{row_print}")

# gets the bottommost empty space in a column

# displays board
print_board()

# displays whose turn it is
print(f"\n{symbols[current_player]}'s turn!")

# asks player which column to place their mark, 
# if column is full, doesn't exist, or causes an error, it repeats
# played = False
# while not played:
#     try:
#         column = int(input("Which column? "))

#         if board[row][column] == " ":
#             board[row][column] = current_player
#             played = True
#         else:
#             raise Exception()
#     except:
#         print("Invalid choice!")
