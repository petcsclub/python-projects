# Variables
shipNames = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
shipeLength = [5, 4, 3, 3, 2]


def setShips():
    '''Get the ship placements of the user'''
    for i in range(len(shipNames)):
        print('Set the position of your' + shipNames[i])


def convert(coords):
    '''Convert coords in the correct form to the 2D array coordinates'''
    if coords.length == 2 and coords[0].isalpha() and coords[1].isnumeric():
        print('cool')


# Game loop
while True:
    print('Welcome to Battleship!')
    setShips()
