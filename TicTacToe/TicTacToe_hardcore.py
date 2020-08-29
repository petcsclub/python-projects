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

def not_last(index, list):
    if index == len(list) - 1:
        return False
    return True

def print_board():
    column_indexes_print = "\n  "
    for column_index in range(len(board[0])):
        column_indexes_print += f"{column_index}   "
    print(column_indexes_print)

    for row_index in range(len(board)):
        row_print = f"{row_index}"
        for column_index in range(len(board[row_index])):
            row_print += f" {board[row_index][column_index]} "
            if not_last(column_index, board[row_index]):
                row_print += "|"
        print(row_print)

        if not_last(row_index, board):
            row_border_print = " "
            for column_index in range(len(board[row_index])):
                row_border_print += "---"
                if not_last(column_index, board[row_index]):
                    row_border_print += "+"
            print(row_border_print)

def all_same(list):
    for item in list:
        if item != list[0] or item == " ":
            return False

    return True

def win():
    for row in board:
        if all_same(row):
            return True

    for column in range(len(board[0])):
        check = []
        for row in board:
            check.append(row[column])
        if all_same(check):
            return True

    check = []
    for index in range(len(board)):
        check.append(board[index][index])
    if all_same(check):
        return True

    check = []
    for index, reverse_index in zip(range(len(board)), reversed(range(len(board)))):
        check.append(board[index][reverse_index])
    if all_same(check):
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
    board = []
    getting_board_size = True
    while getting_board_size:
        try:
            board_size = int(input("What board size? "))

            if board_size <= 0:
                raise Exception()
            else:
                getting_board_size = False
        except:
            print("Invalid choice!")

    for row_size in range(board_size):
        row = []
        for column_size in range(board_size):
            row.append(" ")
        board.append(row)

    game_ongoing = True
    while game_ongoing:
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

    print(f"X's wins: {wins[player_X]}")
    print(f"O's wins: {wins[player_O]}")

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