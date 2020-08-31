# imports
from random import randint, choice
from operator import add
from time import sleep
import os


def setPlayerShips(shipNames, shipLength, playerShipAliveCoords, playerGrid, playerNumber):
    '''Get and set the ship placements of the player'''

    # Get player name
    print("Hello Player " + str(playerNumber))
    playerName = input("What is your name? ").upper()

    print('Set the position of your ships! Tell your opponent to look away from the computer screen.')
    sleep(5)
    printGrid(playerGrid, True, playerName)

    # Loops through ships
    for i in range(len(shipNames)):
        while True:
            print('Set the position of your ' +
                  shipNames[i] + ' of length ' + str(shipLength[i]) + '.')

            # Get start coordinate and check validity
            start = input('Coordinate for the start of your ' +
                          shipNames[i] + '? ')
            startCoords = convert(start)
            if startCoords is None:
                print(
                    'Invalid input. Examples of proper coordinates: a0, B9, c2. Please try again.')
                continue

            # Get end coordinate and check validity
            end = input('Coordinate for the end of your ' +
                        shipNames[i] + '? ')
            endCoords = convert(end)
            if endCoords is None:
                print(
                    'Invalid input. Examples of proper coordinates: a0, B9, c2. Please try again.')
                continue

            # Check valid ship length and ensure they are all on one row/column
            if startCoords[0] == endCoords[0]:
                if abs(startCoords[1]-endCoords[1]) + 1 != shipLength[i]:
                    print(
                        'Invalid ship length. Please try again.')
                    continue
            elif startCoords[1] == endCoords[1]:
                if abs(startCoords[0]-endCoords[0]) + 1 != shipLength[i]:
                    print(
                        'Invalid ship length. Please try again.')
                    continue
            else:
                print(
                    'The start and end of the ship must be on the same row or column. Please try again.')
                continue

            # Check validity of ship placement
            if checkShipPlacement(startCoords, endCoords, i, playerShipAliveCoords, playerGrid):
                printGrid(playerGrid, True, playerName)
                break
            else:
                print('Ships cannot intersect. Please try again.')
                continue

    # Remove ships ('s') from the grid
    for i in range(5):
        for coords in playerShipAliveCoords[i]:
            playerGrid[coords[0]][coords[1]] = ' '

    print("Ships successfully set! You won't be able to see the position of your ships again until the end of the game. Tell your opponent to return as soon as the output is cleared.")
    sleep(5)

    # Clear system output
    os.system('cls' if os.name == 'nt' else 'clear')

    return playerName


def playerTurn(shipNames, opponentGrid, opponentShipsAlive, opponentShipAliveCoords, opponentShipSunkCoords, playerName):
    '''Execute player turn'''

    print("{}'S TURN!".format(playerName))
    printGrid(opponentGrid, False, playerName)
    sunkShip = False

    # Player input and logic
    while True:
        # Get attack coordinate and check validity
        attack = input('Coordinate for your attack this turn? ')
        attackCoords = convert(attack)
        if attackCoords is None:
            print(
                'Invalid input. Examples of proper coordinates: a0, B9, c2. Please try again.')
            continue
        elif opponentGrid[attackCoords[0]][attackCoords[1]] is not ' ':
            print('You have already attacked this coordinate. Please try again.')
            continue

        # Check if attack hit a ship and update grid
        shipIndex = hitShip(attackCoords, opponentShipAliveCoords)
        if shipIndex is -1:
            print("Miss!")
            opponentGrid[attackCoords[0]][attackCoords[1]] = '-'
            break
        else:
            print("Hit!")
            opponentGrid[attackCoords[0]][attackCoords[1]] = 'o'
            # Remove attack coordinate from alive set to sunk set
            opponentShipAliveCoords[shipIndex].remove(attackCoords)
            opponentShipSunkCoords[shipIndex].add(attackCoords)
            # Check if alive set is empty (meaning ship is sunk)
            if len(opponentShipAliveCoords[shipIndex]) == 0:
                sunkShip = True
                print("You have sunk your opponent's " +
                      shipNames[shipIndex] + "!")
                opponentShipsAlive -= 1
                for coords in opponentShipSunkCoords[shipIndex]:
                    opponentGrid[coords[0]][coords[1]] = 'x'
            break

    # Print grid again if ship was sunk
    if sunkShip:
        printGrid(opponentGrid, False, playerName)
    print("END TURN!")
    print("--------------------------------------------------")
    if sunkShip:
        sleep(3)
    sleep(2)
    return opponentShipsAlive


def printGrid(grid, showShips, playerName):
    '''Print the specified grid'''

    # Set title based on isPlayerGrid
    if showShips:
        print("\n{}'S SHIPS".format(playerName))
    else:
        print("\n{}'S ATTACKS".format(playerName))

    # Print grid
    for i in range(-1, 10):
        for j in range(-1, 10):
            # Print first row of letters
            if i == -1:
                if j == -1:
                    print(" ", end=" ")
                elif j == 9:
                    print(chr(j+48))
                else:
                    print(chr(j+48), end=" ")
            else:
                # Print first column on numbers
                if j == -1:
                    print(chr(i+65), end=" ")
                # Print grid
                elif j == 9:
                    print(grid[i][j])
                else:
                    print(grid[i][j], end=" ")
    print("Legend: ' ' = empty | '-' = miss | 'o' = hit | 'x' = sunk | 's' = ship\nNote: you cannot see the position of your opponent's ships until the game is finished\n")


def checkShipPlacement(startCoords, endCoords, shipIndex, shipCoords, grid=None):
    '''Check validity of ship placement and return True if placement is valid, false if not'''

    # Check validity
    if startCoords[0] == endCoords[0]:
        # first coordinate is the same
        if startCoords[1] > endCoords[1]:
            startCoords, endCoords = endCoords, startCoords
        # check validity to ensure coordinate doesn't already contain another ship
        for i in range(startCoords[1], endCoords[1]+1):
            if hitShip((startCoords[0], i), shipCoords, shipIndex) >= 0:
                return False
        # input ships and add to set
        for i in range(startCoords[1], endCoords[1]+1):
            shipCoords[shipIndex].add((startCoords[0], i))
            # Print grid if specified (from player)
            if grid != None:
                grid[startCoords[0]][i] = 's'
        return True
    else:
        # second coordinate is the same
        if startCoords[0] > endCoords[0]:
            startCoords, endCoords = endCoords, startCoords
        # check validity to ensure coordinate doesn't already contain another ship
        for i in range(startCoords[0], endCoords[0]+1):
            if hitShip((i, startCoords[1]), shipCoords, shipIndex) >= 0:
                return False
        # input ships and add to set
        for i in range(startCoords[0], endCoords[0]+1):
            shipCoords[shipIndex].add((i, startCoords[1]))
            # Print grid if specified (from player)
            if grid != None:
                grid[i][startCoords[1]] = 's'
        return True


def convert(coords):
    '''Convert coords in the correct form to the 2D array coordinates'''

    # Check correct length
    if len(coords) == 2:
        # Convert to ASCII
        first = ord(coords[0].upper())
        second = ord(coords[1])
        # Check validity of coordinates
        firstValid = first >= 65 and first <= 74
        secondValid = second >= 48 and second <= 57
        if firstValid and secondValid:
            # Return appropriate tuple
            return(first-65, second-48)


def hitShip(coords, shipCoords, shipIndex=5):
    '''Check if coordinate intersects with existing ship, and return the index of the ship if it does. If not, return -1'''

    # Loop through ships
    for i in range(shipIndex):
        # Check if coordinate is in the set for specified ship
        if coords in shipCoords[i]:
            return i
    return -1


# Declare const variables
shipNames = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
shipLength = [5, 4, 3, 3, 2]

# Full game loop
while True:
    # player2 view of player1's grid, initialize with 10x10 grid of ' '
    playerOneGrid = [[' ' for i in range(10)] for j in range(10)]
    # player1 view of player2's grid, initialize with 10x10 grid of ' '
    playerTwoGrid = [[' ' for i in range(10)] for j in range(10)]
    # Keep track of ships alive for player1 and player2 to determine when to end the game
    playerOneShipsAlive = 5
    playerTwoShipsAlive = 5
    gameLength = 0
    # Track coordinates for ships alive and sunk for both players in order to update char from 'o' to 'x' when the entire ship is sunk. Each index represents 1 ship.
    playerOneShipAliveCoords = [set() for i in range(5)]
    playerOneShipSunkCoords = [set() for i in range(5)]
    playerTwoShipAliveCoords = [set() for i in range(5)]
    playerTwoShipSunkCoords = [set() for i in range(5)]

    print('Welcome to Battleship!')
    print("--------------------------------------------------")
    sleep(2)

    # Set ships for both players
    playerOneName = setPlayerShips(shipNames, shipLength,
                                   playerOneShipAliveCoords, playerOneGrid, 1)
    playerTwoName = setPlayerShips(shipNames, shipLength,
                                   playerTwoShipAliveCoords, playerTwoGrid, 2)

    print("START GAME\n")
    sleep(2)

    # Game loop
    while True:
        gameLength += 1
        # Player1 turn
        playerTwoShipsAlive = playerTurn(shipNames, playerTwoGrid, playerTwoShipsAlive, playerTwoShipAliveCoords,
                                         playerTwoShipSunkCoords, playerOneName)
        # Check if game over
        if playerTwoShipsAlive == 0 and playerOneShipsAlive > 1:
            break

        # Player turn
        playerOneShipsAlive = playerTurn(
            shipNames, playerOneGrid, playerOneShipsAlive, playerOneShipAliveCoords, playerOneShipSunkCoords, playerTwoName)
        # Check if game over
        if playerOneShipsAlive == 0 or playerTwoShipsAlive == 0:
            break

    if playerOneShipsAlive == 0 and playerTwoShipsAlive == 0:
        print('TIE!')
        printGrid(playerTwoGrid, True, playerTwoName)
        printGrid(playerOneGrid, True, playerOneName)
    elif playerOneShipsAlive == 0:
        # Player2 won
        print("{} WON IN {} MOVES!".format(playerTwoName, gameLength))
        # Populate player2 grid with positions of un hit ship coordinates
        for ship in playerTwoShipAliveCoords:
            for coords in ship:
                playerTwoGrid[coords[0]][coords[1]] = 's'
        # Print ships grids
        printGrid(playerTwoGrid, True, playerTwoName)
        printGrid(playerOneGrid, True, playerOneName)
    else:
        # Player1 won
        print("{} WON IN {} MOVES!".format(playerOneName, gameLength))
        # Populate player1 grid with positions of un hit ship coordinates
        for ship in playerOneShipAliveCoords:
            for coords in ship:
                playerOneGrid[coords[0]][coords[1]] = 's'
        # Print ships grids
        printGrid(playerOneGrid, True, playerOneName)
        printGrid(playerTwoGrid, True, playerTwoName)

    sleep(5)
    print("Thanks for playing!")

    # Check if players want to play again
    playAgain = ''
    while True:
        playAgain = input("Would you like to play again? [y/n] ")
        playAgain = playAgain.lower()
        if playAgain == 'y' or playAgain == 'n':
            break
        else:
            print("Invalid input. Please enter either 'y' or 'n'. Please try again.")

    if playAgain == 'y':
        continue
    elif playAgain == 'n':
        break
