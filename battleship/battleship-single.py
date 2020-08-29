# Variables
shipNames = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
shipLength = [5, 4, 3, 3, 2]
# player view of player's grid
playerGrid = [[' ' for i in range(10)] for j in range(10)]
# player view of computer's grid
computerGrid = [[' ' for i in range(10)] for j in range(10)]
playerShipCoords = [set() for i in range(5)]
computerShipCoords = [set() for i in range(5)]


def printGrid(grid):
    '''Print the specified grid'''
    for i in range(-1, 10):
        for j in range(-1, 10):
            if i == -1:
                if j == -1:
                    print("\n ", end=" ")
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
    print("Legend: = ' ' = empty | '-' = miss | 'o' = hit | 'x' = sunk | 's' = ship (only available on your grid)\n")


def setPlayerShips():
    '''Get the ship placements of the player'''
    for i in range(len(shipNames)):
        while True:
            print('Set the position of your ' +
                  shipNames[i] + ' of length ' + str(shipLength[i]) + '.')

            # Get start coordinate and check validity
            start = input('Coordinate for the start of your ' +
                          shipNames[i] + '? ')
            startCoords = convert(start)
            if startCoords is None:
                print('Invalid input. Please try again.')
                continue

            # Get end coordinate and check validity
            end = input('Coordinate for the end of your ' +
                        shipNames[i] + '? ')
            endCoords = convert(end)
            if endCoords is None:
                print('Invalid input. Please try again.')
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
            if checkShipPlacement(startCoords, endCoords, i, playerShipCoords, playerGrid):
                printGrid(playerGrid)
                break
            else:
                print('Ships cannot intersect. Please try again.')
                continue


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


# Game loop
while True:
    print('Welcome to Battleship!')
    setPlayerShips()
    break
