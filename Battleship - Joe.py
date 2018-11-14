from random import randint

#empty list to append later
l = []

#Dictionary of ship keys to be called in shipplacement later
shiplist = {"Destroyer":["U","U"],"Submarine":["U","U","U"],"Cruiser":["U","U","U"],"Battleship":["U","U","U","U"],"AirCraftCarrier":["U","U","U","U","U"]}

#The function that records where ships are placed, will be updated later
def shipMarker(Xcord,Ycord,way):
    if way == "1":
        l[Ycord][Xcord] = "U"
    else:
        l[Xcord][Ycord] = "U"
#The Function that records where strike have been placed
def hitmarker(Xcord,Ycord,):
    if l[Ycord][Xcord] == "U":
        print("You hit a ship!")
        l[Ycord][Xcord] = "x"
    else:
        print("You missed!")
        l[Ycord][Xcord] = "O"

#The function that takes player input for striking and ship placement, verifies the input and calls the appropriate fucntion to make markers
def userinput(PlayerGuess,i,opt,way):
    if PlayerGuess.find(".") and PlayerGuess[0:PlayerGuess.find(".")].isnumeric() and int(PlayerGuess[0:PlayerGuess.find(".")]) < 11 and int(PlayerGuess[PlayerGuess.find(".") + 1:len(PlayerGuess)]) < 11 and PlayerGuess[PlayerGuess.find(".") + 1:len(PlayerGuess)].isnumeric() and int(PlayerGuess[0:PlayerGuess.find(".")]) > 0 and int(PlayerGuess[PlayerGuess.find(".") + 1:len(PlayerGuess)]) > 0:
        x = int(PlayerGuess[0:PlayerGuess.find(".")]) - 1
        y = int(PlayerGuess[PlayerGuess.find(".") + 1:len(PlayerGuess)]) - 1
        x = x + i
        if opt == "ship":
            shipMarker(x,y,way)
            return True
        elif opt == "strike":
            way == None
            hitmarker(x,y,way)
            return True
    else:
        print("Please enter in correct format")
        return False

#Function that Generates the intial board if the optional argument is generate and updates the board in place if it is Update
def BoardGUI(opt="Generate"):#game board
    if opt == "Generate":
        for x in range(10):
            l.append(["_"] * 10)
    elif opt == "Update":
        board = ""
        for b in range(10):
            for j in range(10):
                board = board + l[b][j]
                board = board + " "
            board = board + "\n"
        print(board)
        return board

#Function that checks if the striking player hit a ship.

def Menu():
    print("""
BattleShip, Select An Option:
    View Board  (1)
    Place ships (2)
    Start Game  (3)
    """)
    var = input()
    if var == "1":
        BoardGUI("Update")
        Menu()
    if var == "2":
        shipMenu()
        print("DONE PLACING SHIPS!")
    if var == "3":
        strikeMenu()
        print("DONE STRIKING!")

def shipplacement(ship,placement,way):
    i = 0
    while i < len(shiplist[ship]):
        userinput(placement,i,"ship",way)
        i += 1
    BoardGUI("Update")


def strikeMenu():
    i = 0
    print("""
What would you like todo:
    View Board   (1)
    Strike       (2)
""")
    option = input()
    if option == "1":
        BoardGUI("Update")
        strikeMenu()
    if option == "2":
        PlayerGuess = input("Where would you like to strike: ")
        userinput(PlayerGuess,i,"strike")
        strikeMenu()

def shipMenu():
    print("""
Select a ship to place:
    Destroyer         (1)
    Submarine         (2)
    Cruiser           (3)
    Battleship        (4)
    AirCraftCarrier   (5)
""")
    options = input()
    BoardGUI("Update")
    print("""
Which way would you like to place the ship?
    Horizonatally (1)
    Vertically    (2)
    """)
    way = input()

    placement = input("Where would you like to place the ship?")
    if options == "1":
        shipplacement("Destroyer",placement,way)
        Menu()
    if options == "2":
        shipplacement("Submarine",placement,way)
        Menu()
    if options == "3":
        shipplacement("Cruiser",placement,way)
        Menu()
    if options == "4":
        shipplacement("Battleship",placement,way)
        Menu()
    if options == "5":
        shipplacement("AirCraftCarrier",placement,way)
        Menu()
BoardGUI() #generate
Menu()
