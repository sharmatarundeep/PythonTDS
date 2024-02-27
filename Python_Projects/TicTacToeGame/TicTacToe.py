# Tic Tac Toe Game

#Function to print the board in readable format
def print_board(spots):
    print(spots["1"] + "|" + spots["2"] + "|" + spots["3"])
    print("______")
    print(spots["4"] + "|" + spots["5"] + "|" + spots["6"])
    print("______")
    print(spots["7"] + "|" + spots["8"] + "|" + spots["9"])

# Function to check whose turn is this
def check_turn(turn):
    if turn % 2 ==0:
        return "0"
    else:
        return "X"
    
# Function to check if game is won 
def check_for_win(spots):
    # We need to check vertical cases, horizontal cases and diagonal cases
    if (spots["1"] == spots ["2"] == spots ["3"]) or (spots["4"] == spots ["5"] == spots ["6"]) or (spots["7"] == spots ["8"] == spots ["9"]) :
        return True
    elif (spots["1"] == spots ["4"] == spots ["7"]) or (spots["2"] == spots ["5"] == spots ["8"]) or (spots["3"] == spots ["6"] == spots ["9"]) :
        return True
    elif (spots["1"] == spots ["5"] == spots ["9"]) or (spots["3"] == spots ["5"] == spots ["7"]) :
        return True
    else:
        return False

# Lets create a dictionary with 9 keys and value which we will pass on to the print spots function
spots = {"1":"1", "2":"2", "3":"3", "4":"4", "5":"5", "6":"6","7":"7", "8":"8", "9":"9"}

# Now we need to build the game logic
playing = True # loop variable to control while loop
turn = 0 # to track whose turn is this..
complete = False # to end the game and was it completed with a win or not

print ("################")
print ("This is 2 player game")
print ("Take turn one by one")
print ("################")

while playing:
    #To reset the screen
    #os.system('cls' if os.name == 'nt' else 'clear')
    print_board(spots)
    
    #Get the input from the player
    choice = input("Player " + str((turn%2) +1) + " : Please pick the slot of your choice or press q to quit")
    #If player want to quit
    if choice == 'q':
        print ("Bye!!")
        playing = False
    # to make player enter valid spot input 
    elif 1 <= int(choice) <= 9 : 
        # Check if spot is available and not already taken
        if not spots[choice] in ["X" , "0"]:
            # valid input
            turn += 1
            spots[choice] = check_turn(turn)
    # check if someone has won and hence game has ended 
    if check_for_win(spots):
        playing,complete = False, True
    # now handle the case where all turns taken and no one won
    if turn > 8 :
        playing = False

# out of the while loop
# draw the board one last final time
print_board(spots)
if complete:
    if check_turn == "X": # if last change before winning was by player 1 
        print("Player 1 Wins!!")
    else:
        print("Player 2 Wins!!")
else :
    print ("No winner")

print ("Thanks for playing")