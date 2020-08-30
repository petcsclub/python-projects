from random import randint, choice
from operator import add
from time import sleep


def setPlayerShips(shipNames, shipLength, playerShipAliveCoords, playerGrid):
    '''Set the ship placements of the player'''
    print('Set the position of your ships!')
    printGrid(playerGrid, True)
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

            # Check valid ship length and row/column
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
    for i in range(len(shipNames)):
        while True:
            startCoords = (randint(0, 9), randint(0, 9))
            endCoords = tuple(map(add, startCoords, choice(
                [(0, shipLength[i]-1), (shipLength[i]-1, 0)])))
            if endCoords[0] < 0 or endCoords[0] > 9 or endCoords[1] < 0 or endCoords[1] > 9:
                continue

            if checkShipPlacement(startCoords, endCoords, i, computerShipAliveCoords):
                print(str(startCoords) + str(endCoords))
                break
            else:
                continue


def playerTurn(shipNames, computerGrid, computerShipsAlive, computerShipAliveCoords, computerShipSunkCoords):
    print("YOUR TURN!")
    printGrid(computerGrid, False)
    sunkShip = False
    while True:
        attack = input('Coordinate for your attack this turn? ')
        attackCoords = convert(attack)
        if attackCoords is None:
            print(
                'Invalid input. Examples of proper coordinates: a0, B9, c2. Please try again.')
            continue
        elif computerGrid[attackCoords[0]][attackCoords[1]] is not ' ':
            print('You have already attacked this coordinate. Please try again.')
            continue

        shipIndex = hitShip(attackCoords, computerShipAliveCoords)
        if shipIndex is -1:
            print("Miss!")
            computerGrid[attackCoords[0]][attackCoords[1]] = '-'
            break
        else:
            print("Hit!")
            computerGrid[attackCoords[0]][attackCoords[1]] = 'o'
            computerShipAliveCoords[shipIndex].remove(attackCoords)
            computerShipSunkCoords[shipIndex].add(attackCoords)
            if len(computerShipAliveCoords[shipIndex]) == 0:
                sunkShip = True
                print("You have sunk the computer's " +
                      shipNames[shipIndex] + "!")
                computerShipsAlive -= 1
                for coords in computerShipSunkCoords[shipIndex]:
                    computerGrid[coords[0]][coords[1]] = 'x'
            break

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
    attackCoords = choice(tuple(computerAvailableAttacks))
    computerAvailableAttacks.remove(attackCoords)
    sunkShip = False
    print('The computer attacked coordinate ' +
          chr(attackCoords[0]+65) + chr(attackCoords[1]+48) + '.')
    shipIndex = hitShip(attackCoords, playerShipAliveCoords)
    if shipIndex is -1:
        print("Miss!")
        playerGrid[attackCoords[0]][attackCoords[1]] = '-'
    else:
        print("Hit!")
        playerGrid[attackCoords[0]][attackCoords[1]] = 'o'
        playerShipAliveCoords[shipIndex].remove(attackCoords)
        playerShipSunkCoords[shipIndex].add(attackCoords)
        if len(playerShipAliveCoords[shipIndex]) == 0:
            sunkShip = True
            print("The computer sunk your " +
                  shipNames[shipIndex] + "!")
            playerShipsAlive -= 1
            for coords in playerShipSunkCoords[shipIndex]:
                playerGrid[coords[0]][coords[1]] = 'x'

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
    if isPlayerGrid:
        print("\n      YOUR SHIPS")
    else:
        print("\n     YOUR ATTACKS")
    for i in range(-1, 10):
        for j in range(-1, 10):
            if i == -1:
                if j == -1:
                    print(" ", end=" ")
                elif j == 9:
                    print(chr(j+48))
                else:
                    print(chr(j+48), end=" ")
            else:
                if j == -1:
                    print(chr(i+65), end=" ")
                elif j == 9:
                    print(grid[i][j])
                else:
                    print(grid[i][j], end=" ")
    print("Legend: ' ' = empty | '-' = miss | 'o' = hit | 'x' = sunk | 's' = ship\nNote: you cannot see the position of the computer's ships until the game is finished\n")


def checkShipPlacement(startCoords, endCoords, shipIndex, shipCoords, grid=None):
    # Check validity
    if startCoords[0] == endCoords[0]:
        # first coordinate is the same
        if startCoords[1] > endCoords[1]:
            startCoords, endCoords = endCoords, startCoords
        # check validity
        for i in range(startCoords[1], endCoords[1]+1):
            if hitShip((startCoords[0], i), shipCoords, shipIndex) >= 0:
                return False
        # input ships
        for i in range(startCoords[1], endCoords[1]+1):
            shipCoords[shipIndex].add((startCoords[0], i))
            if grid != None:
                grid[startCoords[0]][i] = 's'
        return True
    else:
        # second coordinate is the same
        if startCoords[0] > endCoords[0]:
            startCoords, endCoords = endCoords, startCoords
        # check validity
        for i in range(startCoords[0], endCoords[0]+1):
            if hitShip((i, startCoords[1]), shipCoords, shipIndex) >= 0:
                return False
        # input ships
        for i in range(startCoords[0], endCoords[0]+1):
            shipCoords[shipIndex].add((i, startCoords[1]))
            if grid != None:
                grid[i][startCoords[1]] = 's'
        return True


def convert(coords):
    '''Convert coords in the correct form to the 2D array coordinates'''
    if len(coords) == 2:
        first = ord(coords[0].upper())
        second = ord(coords[1])
        firstValid = first >= 65 and first <= 74
        secondValid = second >= 48 and second <= 57
        if firstValid and secondValid:
            return(first-65, second-48)


def hitShip(coords, shipCoords, shipIndex=5):
    '''Check if coordinate intersects with existing ship, and return the index of the ship if it does. If not, return -1'''
    for i in range(shipIndex):
        if coords in shipCoords[i]:
            return i
    return -1


# Declare variables
shipNames = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
shipLength = [5, 4, 3, 3, 2]

# Game loop
while True:
    # player view of player's grid
    playerGrid = [[' ' for i in range(10)] for j in range(10)]
    # player view of computer's grid
    computerGrid = [[' ' for i in range(10)] for j in range(10)]
    playerShipsAlive = 5
    computerShipsAlive = 5
    playerShipAliveCoords = [set() for i in range(5)]
    playerShipSunkCoords = [set() for i in range(5)]
    computerShipAliveCoords = [set() for i in range(5)]
    computerShipSunkCoords = [set() for i in range(5)]
    computerAvailableAttacks = set()
    gameLength = 0

    for i in range(10):
        for j in range(10):
            computerAvailableAttacks.add((i, j))

    print('Welcome to Battleship!')
    print("--------------------------------------------------")
    sleep(2)
    setComputerShips(shipNames, shipLength, computerShipAliveCoords)
    setPlayerShips(shipNames, shipLength, playerShipAliveCoords, playerGrid)

    while True:
        gameLength += 1
        computerShipsAlive = playerTurn(shipNames, computerGrid, computerShipsAlive, computerShipAliveCoords,
                                        computerShipSunkCoords)
        if computerShipsAlive == 0:
            break

        playerShipsAlive = computerTurn(shipNames, playerGrid, playerShipsAlive,
                                        playerShipAliveCoords, playerShipSunkCoords, computerAvailableAttacks)
        if playerShipsAlive == 0:
            break

    if computerShipsAlive == 0:
        print("YOU WON IN {} MOVES!".format(gameLength))
        printGrid(playerGrid, True)
        printGrid(computerGrid, False)
    else:
        print("YOU LOST!")
        printGrid(playerGrid, True)
        for ship in computerShipAliveCoords:
            for coords in ship:
                computerGrid[coords[0]][coords[1]] = 's'
        printGrid(computerGrid, False)

    sleep(5)
    print("Thanks for playing!")

    while True:
        playAgain = input("Would you like to play again? [y/n] ")
        playAgain = playAgain.lower()
        if playAgain == 'y':
            continue
        elif playAgain == 'n':
            break
        else:
            print("Invalid input. Please enter either 'y' or 'n'. Please try again.")
