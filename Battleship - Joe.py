from random import randint

l = [] #empty list to append later

Boatlist = {"Destroyer":["U","U"],"Submarine":["U","U","U"],"Cruiser":["U","U","U"],"Battleship":["U","U","U","U"],"AirCraftCarrier":["U","U","U","U","U"]}

def BoatMarker(Xcord,Ycord):
    l[Ycord][Xcord] = "U"

def hitmarker(Xcord,Ycord):
    l[Ycord][Xcord] = "x"

def userinput(opt=""):
    if opt == "ship":
        PlayerGuess = input("Where should we place the ship? (x,y): ")
        x = int(PlayerGuess[0:PlayerGuess.find(".")]) - 1
        y = int(PlayerGuess[PlayerGuess.find(".") + 1:len(PlayerGuess)]) - 1
        BoatMarker(x,y)
    if opt == "strike":
        PlayerGuess = input("Missle strike to space? (x,y): ")
        x = int(PlayerGuess[0:PlayerGuess.find(".")]) - 1
        y = int(PlayerGuess[PlayerGuess.find(".") + 1:len(PlayerGuess)]) - 1
        HitChecker(x,y)
        hitmarker(x,y)

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

def HitChecker(Xcord,Ycord):
    if l[Ycord][Xcord] == "U":
        print("You hit a ship!")
    else:
        print("You missed!")




BoardGUI() #generate
for i in range(5):
    userinput("ship")
    BoardGUI("Update")
print("DONE PLACING SHIPS!")
for i in range(5):
    userinput("strike")
    BoardGUI("Update")
print("DONE STRIKING!")
