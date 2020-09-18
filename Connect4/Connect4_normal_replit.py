def print_board(board, symbols):
    """Print out the board."""

    # creates string that will label each board column with their label
    column_indexes_print = "\n"

    # adds the index of each board column (converted to emoji form) to column_indexes_print
    for column_index in range(len(board[0])):
        column_indexes_print += symbols[column_index]

    # prints string of board columns
    print(column_indexes_print)

    # repeats for each row in board
    for row in range(len(board)):
        # creates string that represents each value in the row
        row_print = ""

        # adds each value in the row (converted to emoji form) to row_print
        for space in board[row]:
            row_print += symbols[space]

        # print out all the values in the row
        print(row_print)


def bottom_row(column, board):
    """Return the bottommost empty space in a column."""
    for row in reversed(range(len(board))):
        if board[row][column] == " " and column >= 0:
            return row

    return -1


def switch_player(current_player, players):
    """Switch the current player"""
    if current_player == players[0]:
        return players[1]
    else:
        return players[0]


def all_same(l):
    """Take in a list, return whether all its elements are the same."""
    return l.count("r") == 4 or l.count("y") == 4


def win(board):
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


def tie(board):
    """Return whether the game is a tie"""
    for row in board:
        for space in row:
            if space == " ":
                return False

    return True


def run_connect4_normal():
    board = [[" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "]]

    symbols = {
        "r": "🔴  ",
        "y": "🟡  ",
        " ": "⚪  ",
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

    players = ["r", "y"]
    current_player = players[0]

    # main game loop
    while True:
        # displays board
        print_board(board, symbols)

        # displays whose turn it is
        print(f"\n{symbols[current_player]}'s turn!")

        # asks player which column to place their circle, 
        # if column is occupied, doesn't exist, or causes an error, it repeats
        while True:
            column = input("Which column? ")

            if (
                column.isdigit() and
                int(column) < 7 and
                board[bottom_row(int(column), board)][int(column)] == " "
            ):
                board[bottom_row(int(column), board)][int(column)] = current_player
                break
            else:
                print("Invalid choice!")

        # if someone wins or there's a tie, displays the winner and ends the main game loop
        # if not, gives turn to next player and repeats main game loop
        if win(board):
            print_board(board, symbols)
            print(f"\n{symbols[current_player]} wins!")
            break
        elif tie(board):
            print_board(board, symbols)
            print(f"\nTie!")
            break
        else:
            current_player = switch_player(current_player, players)


if __name__ == "__main__":
    run_connect4_normal()