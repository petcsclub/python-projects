from time import sleep
from battleship.battleship_single import runBattleshipSingle
from battleship.battleship_multi import runBattleshipMulti
from TicTacToe.TicTacToe_normal import run_tictactoe_normal
from TicTacToe.TicTacToe_hardcore import run_tictactoe_hardcore
from Connect4.Connect4_normal_replit import run_connect4_normal
from Connect4.Connect4_hardcore_replit import run_connect4_hardcore
from madlibs.madlibs import runMadlibs
from madlibs.madlibs_custom import runMadlibsCustom
from text_adventure import runTextAdventure
from Hangman.HangmanEasy import runHangmanEasy
from Hangman.HangmanAdv import runHangmanAdv


class bc:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    END = '\033[0m'


while True:
    print('Welcome to the PETCS Intro to Python Projects Demo! Here are all the available games:\n')
    print(bc.BLUE + 'MEDIUM' + bc.END)
    print('0: Madlibs')
    print('1: Madlibs Custom')
    print('2: Tic-Tac-Toe')
    print('3: Tic-Tac-Toe Hardcore')
    print('4: Connect 4')
    print('5: Connect 4 Hardcore')
    print('6: Text Adventure\n')

    print(bc.GREEN + 'HARD' + bc.END)
    print('7: Hangman Easy')
    print('8: Hangman Hard')
    print('9: Battleship Multiplayer')
    print('10: Battleship Singleplayer\n')

    choice = ''
    while True:
        choice = input(
            'Which game would you like to play? Please enter an integer from 0 to 10: ')
        if choice.isdecimal() and int(choice) >= 0 and int(choice) <= 10:
            break
        else:
            print('Invalid input. Please enter an integer from 0 to 10.')

    print('Enjoy! Note: if you would like to quit the game, do Ctrl + C. Then click the "run again" button at the bottom of the screen.\n')
    sleep(2)

    if choice == '0':
        runMadlibs()
    elif choice == '1':
        runMadlibsCustom()
    elif choice == '2':
        run_tictactoe_normal()
    elif choice == '3':
        run_tictactoe_hardcore()
    elif choice == '4':
        run_connect4_normal()
    elif choice == '5':
        run_connect4_hardcore()
    elif choice == '6':
        runTextAdventure()
    elif choice == '7':
        runHangmanEasy()
    elif choice == '8':
        runHangmanAdv()
    elif choice == '9':
        runBattleshipMulti()
    elif choice == '10':
        runBattleshipSingle()

    print('Hope you enjoyed playing! Returning to main menu...\n')
    sleep(2)
