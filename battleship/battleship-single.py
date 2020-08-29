# Variables
shipNames = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
shipLength = [5, 4, 3, 3, 2]
playerGrid = [[' ' for i in range(10)] for j in range(10)]
computerGrid = [[' ' for i in range(10)] for j in range(10)]
playerShipCoords = {}
computerShipCoords = {}


def setPlayerShips():
    '''Get the ship placements of the player'''
    for i in range(len(shipNames)):
        while True:
            print('Set the position of your' +
                  shipNames[i] + ' of length ' + shipLength[i] + '.')

            # Get start coordinate and check validity
            first = input('Coordinate for the start of your ' +
                          shipNames[i] + '?')
            firstCoords = convert(first)
            if firstCoords is None:
                print('Invalid input. Please try again.')
                continue

            # Get end coordinate and check validity
            second = input('Coordinate for the end of your ' +
                           shipNames[i] + '?')
            secondCoords = convert(second)
            if secondCoords is None:
                print('Invalid input. Please try again.')
                continue

            # Check valid ship length and row/column
            if firstCoords[0] == secondCoords[0]:
                if abs(firstCoords[1]-secondCoords[1]) + 1 != shipLength[i]:
                    print(
                        'Invalid ship length. Please try again')
                    continue
            elif firstCoords[1] == secondCoords[1]:
                if abs(firstCoords[0]-secondCoords[0]) + 1 != shipLength[i]:
                    print(
                        'Invalid ship length. Please try again')
                    continue
            else:
                print(
                    'The start and end of the ship must be on the same row or column. Please try again')
                continue


def convert(coords):
    '''Convert coords in the correct form to the 2D array coordinates'''
    first = ord(coords[0].upper())
    second = coords[1]
    firstValid = first >= 65 and first <= 74
    secondValid = second >= 48 and second <= 57
    if coords.length == 2 and firstValid and secondValid:
        return(first-65, second-48)


# Game loop
while True:
    print('Welcome to Battleship!')
    break
    # setShips()
