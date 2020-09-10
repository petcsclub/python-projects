from time import sleep


class bc:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    END = '\033[0m'


while True:
    print('Welcome to the PETCS Projects Demo! Here are all the available games:\n')
    print(bc.BLUE + 'MEDIUM' + bc.END)
    print('0: Madlibs')
    print('1: Madlibs Custom')
    print('2: Tic-Tac-Toe')
    print('3: Tic-Tac-Toe Hardcore')
    print('4: Connect 4')
    print('5: Connect 4 Hardcore')
    print('6: Text Adventure\n')

    print(bc.GREEN + 'HARD' + bc.END)
    print('7: Hangman')
    print('8: Battleship Multiplayer')
    print('9: Battleship Singleplayer\n')

    choice = input(
        'Which game would you like to play? Please enter an integer from 0 to 9: ')

    print('Enjoy! Note: if you would like to quit the game, do Ctrl + C. Then click the "run again" button at the bottom of the screen.')
    sleep(2)
