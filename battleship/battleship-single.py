# imports
from random import randint, choice
from operator import add
from time import sleep


def setPlayerShips(shipNames, shipLength, playerShipAliveCoords, playerGrid):
    '''Get and set the ship placements of the player'''

    print('Set the position of your ships!')
    printGrid(playerGrid, True)

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
                printGrid(playerGrid, True)
                break
            else:
                print('Ships cannot intersect. Please try again.')
                continue

    print("Ships successfully set!")
    sleep(2)
    print("--------------------------------------------------")
    print("START GAME\n")
    sleep(2)


def setComputerShips(shipNames, shipLength, computerShipAliveCoords):
    '''Set the ship placements of the computer'''

    # Loops through ships
    for i in range(len(shipNames)):
        while True:
            # Get random start coordinate
            startCoords = (randint(0, 9), randint(0, 9))
            # Get random end coordinate from start coordinate to ensure proper ship length
            endCoords = tuple(map(add, startCoords, choice(
                [(0, shipLength[i]-1), (shipLength[i]-1, 0)])))
            # Ensure end coordinate is on the grid
            if endCoords[0] < 0 or endCoords[0] > 9 or endCoords[1] < 0 or endCoords[1] > 9:
                continue
            # Check validity of ship placement
            if checkShipPlacement(startCoords, endCoords, i, computerShipAliveCoords):
                print(str(startCoords) + str(endCoords))
                break
            else:
                continue


def playerTurn(shipNames, computerGrid, computerShipsAlive, computerShipAliveCoords, computerShipSunkCoords):
    '''Execute player turn'''

    print("YOUR TURN!")
    printGrid(computerGrid, False)
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
        elif computerGrid[attackCoords[0]][attackCoords[1]] is not ' ':
            print('You have already attacked this coordinate. Please try again.')
            continue

        # Check if attack hit a ship and update grid
        shipIndex = hitShip(attackCoords, computerShipAliveCoords)
        if shipIndex is -1:
            print("Miss!")
            computerGrid[attackCoords[0]][attackCoords[1]] = '-'
            break
        else:
            print("Hit!")
            computerGrid[attackCoords[0]][attackCoords[1]] = 'o'
            # Remove attack coordinate from alive set to sunk set
            computerShipAliveCoords[shipIndex].remove(attackCoords)
            computerShipSunkCoords[shipIndex].add(attackCoords)
            # Check if alive set is empty (meaning ship is sunk)
            if len(computerShipAliveCoords[shipIndex]) == 0:
                sunkShip = True
                print("You have sunk the computer's " +
                      shipNames[shipIndex] + "!")
                computerShipsAlive -= 1
                for coords in computerShipSunkCoords[shipIndex]:
                    computerGrid[coords[0]][coords[1]] = 'x'
            break

    # Print grid again if ship was sunk
    if sunkShip:
        printGrid(computerGrid, False)
    print("END TURN!")
    print("--------------------------------------------------")
    if sunkShip:
        sleep(3)
    sleep(2)
    return computerShipsAlive


def computerTurn(shipNames, playerGrid, playerShipsAlive, playerShipAliveCoords, playerShipSunkCoords, computerAvailableAttacks):
    '''Execute computer turn'''

    print("COMPUTER TURN!")
    printGrid(playerGrid, True)
    sleep(2)
    # Get random attack coordinate from available attacks set
    attackCoords = choice(tuple(computerAvailableAttacks))
    computerAvailableAttacks.remove(attackCoords)
    sunkShip = False
    print('The computer attacked coordinate ' +
          chr(attackCoords[0]+65) + chr(attackCoords[1]+48) + '.')
    shipIndex = hitShip(attackCoords, playerShipAliveCoords)

    # Check if attack hit a ship and update grid
    if shipIndex is -1:
        print("Miss!")
        playerGrid[attackCoords[0]][attackCoords[1]] = '-'
    else:
        print("Hit!")
        playerGrid[attackCoords[0]][attackCoords[1]] = 'o'
        # Remove attack coordinate from alive set to sunk set
        playerShipAliveCoords[shipIndex].remove(attackCoords)
        playerShipSunkCoords[shipIndex].add(attackCoords)
        # Check if alive set is empty (meaning ship is sunk)
        if len(playerShipAliveCoords[shipIndex]) == 0:
            sunkShip = True
            print("The computer sunk your " +
                  shipNames[shipIndex] + "!")
            playerShipsAlive -= 1
            for coords in playerShipSunkCoords[shipIndex]:
                playerGrid[coords[0]][coords[1]] = 'x'

    # Print grid again if ship was sunk
    if sunkShip:
        printGrid(playerGrid, True)
    print("END TURN!")
    print("--------------------------------------------------")
    if sunkShip:
        sleep(3)
    sleep(2)
    return playerShipsAlive


def printGrid(grid, isPlayerGrid):
    '''Print the specified grid'''

    # Set title based on isPlayerGrid
    if isPlayerGrid:
        print("\n      YOUR SHIPS")
    else:
        print("\n     YOUR ATTACKS")

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
    print("Legend: ' ' = empty | '-' = miss | 'o' = hit | 'x' = sunk | 's' = ship\nNote: you cannot see the position of the computer's ships until the game is finished\n")


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
    # player view of player's grid, initialize with 10x10 grid of ' '
    playerGrid = [[' ' for i in range(10)] for j in range(10)]
    # player view of computer's grid, initialize with 10x10 grid of ' '
    computerGrid = [[' ' for i in range(10)] for j in range(10)]
    # Keep track of ships alive for player and computer to determine when to end the game
    playerShipsAlive = 5
    computerShipsAlive = 5
    gameLength = 0
    # Track coordinates for ships alive and sunk for both player and computer in order to update char from 'o' to 'x' when the entire ship is sunk. Each index represents 1 ship.
    playerShipAliveCoords = [set() for i in range(5)]
    playerShipSunkCoords = [set() for i in range(5)]
    computerShipAliveCoords = [set() for i in range(5)]
    computerShipSunkCoords = [set() for i in range(5)]

    # Set of all computer available attacks
    computerAvailableAttacks = set()
    for i in range(10):
        for j in range(10):
            computerAvailableAttacks.add((i, j))

    print('Welcome to Battleship!')
    print("--------------------------------------------------")
    sleep(2)

    # Set ships for computer and player
    setComputerShips(shipNames, shipLength, computerShipAliveCoords)
    setPlayerShips(shipNames, shipLength, playerShipAliveCoords, playerGrid)

    # Game loop
    while True:
        gameLength += 1
        # Computer turn
        computerShipsAlive = playerTurn(shipNames, computerGrid, computerShipsAlive, computerShipAliveCoords,
                                        computerShipSunkCoords)
        # Check if game over
        if computerShipsAlive == 0:
            break

        # Player turn
        playerShipsAlive = computerTurn(shipNames, playerGrid, playerShipsAlive,
                                        playerShipAliveCoords, playerShipSunkCoords, computerAvailableAttacks)
        # Check if game over
        if playerShipsAlive == 0:
            break

    if computerShipsAlive == 0:
        # Player won
        print("YOU WON IN {} MOVES!".format(gameLength))
        printGrid(playerGrid, True)
        printGrid(computerGrid, False)
    else:
        # Computer won
        print("YOU LOST!")
        printGrid(playerGrid, True)
        # Populate computer grid with positions of un hit ship coordinates
        for ship in computerShipAliveCoords:
            for coords in ship:
                computerGrid[coords[0]][coords[1]] = 's'
        printGrid(computerGrid, False)

    sleep(5)
    print("Thanks for playing!")

    # Check if player wants to play again
    while True:
        playAgain = input("Would you like to play again? [y/n] ")
        playAgain = playAgain.lower()
        if playAgain == 'y':
            continue
        elif playAgain == 'n':
            break
        else:
            print("Invalid input. Please enter either 'y' or 'n'. Please try again.")
