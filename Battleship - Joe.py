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
        if PlayerGuess.find(".") and PlayerGuess[0:PlayerGuess.find(".")].isnumeric() and int(PlayerGuess[0:PlayerGuess.find(".")]) < 11 and int(PlayerGuess[PlayerGuess.find(".") + 1:len(PlayerGuess)]) < 11 and PlayerGuess[PlayerGuess.find(".") + 1:len(PlayerGuess)].isnumeric() and int(PlayerGuess[0:PlayerGuess.find(".")]) > 0 and int(PlayerGuess[PlayerGuess.find(".") + 1:len(PlayerGuess)]) > 0:
            x = int(PlayerGuess[0:PlayerGuess.find(".")]) - 1
            y = int(PlayerGuess[PlayerGuess.find(".") + 1:len(PlayerGuess)]) - 1
            BoatMarker(x,y)
            return True
        else:
            print("Please enter in correct format")
            return False
    if opt == "strike":
        PlayerGuess = input("Missle strike to space? (x,y): ")
        if PlayerGuess.find(".") and PlayerGuess[0:PlayerGuess.find(".")].isnumeric() and int(PlayerGuess[0:PlayerGuess.find(".")]) < 11 and int(PlayerGuess[PlayerGuess.find(".") + 1:len(PlayerGuess)]) < 11 and PlayerGuess[PlayerGuess.find(".") + 1:len(PlayerGuess)].isnumeric() and int(PlayerGuess[0:PlayerGuess.find(".")]) > 0 and int(PlayerGuess[PlayerGuess.find(".") + 1:len(PlayerGuess)]) > 0:
            x = int(PlayerGuess[0:PlayerGuess.find(".")]) - 1
            y = int(PlayerGuess[PlayerGuess.find(".") + 1:len(PlayerGuess)]) - 1
            HitChecker(x,y)
            hitmarker(x,y)
            return True
        else:
            print("Please enter in correct format")
            return False


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
count = 1
while count < 6:
    numcheck = userinput("ship")
    if numcheck == False:
        count -= 1
    else:
        BoardGUI("Update")
    count += 1
print("DONE PLACING SHIPS!")
count = 1
while count < 6:
    numcheck = userinput("strike")
    if numcheck == False:
        count -= 1
    else:
        BoardGUI("Update")
    count += 1
print("DONE STRIKING!")
