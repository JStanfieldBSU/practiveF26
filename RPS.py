# Necessary library for the RPS AI to function
import random

# Holds the last move the player made across functions
lastMove = "temp"

# Handles reused code for verifying user input for confirmations
def confirmFunction():
	print("Y/N")
	confVar = input()
	if(confVar == ("Y") or confVar == ("y")):
		return True
	elif(confVar == ("N") or confVar == ("n")):
		return False
	else:
		print("You have input an invalid value, please try again.");
		confirmFunction()

# Handles the 'AI' of the Rock Paper Scissors game
def rpsMoveSelect():
    global lastMove
    # checkOne decides if the AI should change strategy
    checkOne = random.randint(1,2)
    # checkTwo decides if the AI should pick the winning or losing move against the user's last played hand.
    checkTwo = random.randint(1,2)
    if(checkOne == 2):
        if(checkTwo == 2):
            if(lastMove == ("1")):
                moveChoice = "2"
            elif(lastMove == ("2")):
                moveChoice = "3"
            else:
                moveChoice = "1"
        else:
            if(lastMove == ("1")):
                moveChoice = "3"
            elif(lastMove == ("2")):
                moveChoice = "1"
            else:
                moveChoice = "2"
    else:
        moveChoice = str(random.randint(1,3))
    if(moveChoice == "1"):
        print("Opponent chose Rock")
    elif(moveChoice == "2"):
        print("Opponent chose Paper")
    else:
        print("Opponent chose Scissors")
    return moveChoice

# Handles the gameplay of the Rock Paper Scissors Minigame
def rpsFunction():
    global lastMove
    print("Let's play Rock Paper Scissors!")
    print("""Please select your move. I promise I won't peak!
    1 for Rock
    2 for Paper
    3 for Scissors""")
    print("Please type the number for the move you'd like to make!")
    currentMove = input();
    if(currentMove != ("1") and currentMove != ("2") and currentMove != ("3")):
       print("You have selected an invalid option, please try again!")
       rpsFunction()
    else:
       if(lastMove == "temp"):
        lastMove = currentMove
    computerMove = rpsMoveSelect()
    if(currentMove == ("1")):
       if(computerMove == ("1")):
        print("Rock ties with itself!")
       elif(computerMove == ("2")):
        print("Rock loses to Paper!")
       else:
        print("Rock wins against Scissors!")
    elif(currentMove == ("2")):
       if(computerMove == ("1")):
        print("Paper wins against Rock!")
       elif(computerMove == ("2")):
        print("Paper ties with itself!")
       else:
        print("Paper loses to Scissors!")
    else:
        if(computerMove == ("1")):
            print("Scissors loses to Rock!")
        elif(computerMove == ("2")):
            print("Scissors wins against Paper!")
        else:
            print("Scissors ties with itself!")
    lastMove = currentMove
    print("Would you like to play again?")
    if(confirmFunction()):
        rpsFunction()
    else:
        return

# Main body of the program
print("Please input your name!")
userName = input()

print("Hello " + userName + "!")
print("Would you like to play a game?")
# Entry to the rpsFunction Loop
if(confirmFunction()):
    rpsFunction()
# End of Program, reached after selecting 'N' or 'n' in any instance of the confirmFunction
print(userName + ", thank you so much for playing!")	
