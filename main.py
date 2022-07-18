import subprocess
import json
import sys
import pickle
from os import path
from trueskill import Rating, rate_1vs1
import trueskill


initialElo = 1000.0
trueskill.setup(initialElo,initialElo/3,initialElo/6,initialElo/300,0.25,None)

#load in player history
try:
    with open("playerHistory.pickle","rb") as f:
        playerHistory = pickle.load(f)

except (OSError) as e:
    playerHistory = {}
    with open("playerHistory.pickle","wb") as f:
        pickle.dump(playerHistory, f)



print(playerHistory)
#store players
player1 = sys.argv[1]
player2 = sys.argv[2]

if player1 not in playerHistory.keys(): #new player


    #check if player 1 is bot or human
    if path.exists(player1):
        print("Player 1 is an existing bot")
        playerHistory[player1] = {'IsComputer':1, 'X ELO':initialElo, 'X Confidence':initialElo/3, 'X Wins':0, 'X Losses':0, 'X Draws':0, 'O ELO':initialElo, 'O Confidence': initialElo/3, 'O Wins':0, 'O Losses':0, 'O Draws':0}
    else:
        if ".py" in player1:
            print("Player 1 is referencing a bot not included in the folder")
            exit()
        else:
            print("Player 1 is a human")
            playerHistory[player1] = {'IsComputer':0, 'X ELO':initialElo, 'X Confidence':initialElo/3, 'X Wins':0, 'X Losses':0, 'X Draws':0, 'O ELO':initialElo, 'O Confidence': initialElo/3, 'O Wins':0, 'O Losses':0, 'O Draws':0}

if player2 not in playerHistory.keys(): #new player
    #check if player 2 is bot or human
    if path.exists(player2):
        print("Player 2 is an existing bot")
        playerHistory[player2] = {'IsComputer':1, 'X ELO':initialElo, 'X Confidence':initialElo/3, 'X Wins':0, 'X Losses':0, 'X Draws':0, 'O ELO':initialElo, 'O Confidence': initialElo/3, 'O Wins':0, 'O Losses':0, 'O Draws':0}
    else:
        if ".py" in player2:
            print("Player 2 is referencing a bot not included in the folder")
            exit()
        else:
            print("Player 2 is a human")
            playerHistory[player2] = {'IsComputer':0, 'X ELO':initialElo, 'X Confidence':initialElo/3, 'X Wins':0, 'X Losses':0, 'X Draws':0, 'O ELO':initialElo, 'O Confidence': initialElo/3, 'O Wins':0, 'O Losses':0, 'O Draws':0}
print(playerHistory)
position = [
        [" ", " ", " "," ", " ", " "," "],
        [" ", " ", " "," ", " ", " "," "],
        [" ", " ", " "," ", " ", " "," "],
        [" ", " ", " "," ", " ", " "," "],
        [" ", " ", " "," ", " ", " "," "],
        [" ", " ", " "," ", " ", " "," "]
    ]

def printBoard(position):
        print("***********************************")
        for row in position:
            print(row)
        print("***********************************")

def checkForWin(position):
    
    #check across
    for row in position:
        for i in range(4):
            if row[0+i] == row[1+i] == row[2+i] == row[3+i] and row[0+i] != " ":
                return True

    #check verical
    for i in range(len(position[0])):
        for j in range(3):
            if position[0+j][i] == position[1+j][i] == position[2+j][i] == position[3+j][i] and position[0+j][i] != " ":
                return True

    #check down diagonal
    for i in range(len(position[0])-3): #col
        for j in range(len(position)-3): #row
            if position[0+j][0+i] == position[1+j][1+i] == position[2+j][2+i] == position[3+j][3+i] and position[0+j][0+i] != " ":
                return True

    #check up diagonal
    for i in range(len(position[0])-3): #col
        for j in range(len(position)-3): #row
            if position[5-j][0+i] == position[4-j][1+i] == position[3-j][2+i] == position[2-j][3+i] and position[5-j][0+i] != " ":
                return True
    
    return False

def checkForDraw(position):
    #check if spots available
    for row in position:
        for val in row:
            if val == " ":
                return False
    return True

def insertLetter(position, letter, coordinates):
    x,y = coordinates
    if position[x][y] == ' ':
        position[x][y] = letter
        printBoard(position)
        if (checkForDraw(position)):

            print("Draw!")
            player1Rating = Rating(playerHistory[player1]['X ELO'],playerHistory[player1]['X Confidence'])
            player2Rating = Rating(playerHistory[player2]['O ELO'],playerHistory[player2]['O Confidence'])
            player1Rating, player2Rating = rate_1vs1(player1Rating, player2Rating, drawn=True)
            playerHistory[player1]['X ELO'] = player1Rating.mu
            playerHistory[player1]['X Confidence'] = player1Rating.sigma
            playerHistory[player2]['O ELO'] = player2Rating.mu
            playerHistory[player2]['O Confidence'] = player2Rating.sigma
            playerHistory[player2]['O Draws'] += 1 
            playerHistory[player1]['X Draws'] += 1
            playerHistory[player2]['O Draws'] += 1 

        elif checkForWin(position):

            if letter == "X":

                print("Player 1 Wins!")
                player1Rating = Rating(playerHistory[player1]['X ELO'],playerHistory[player1]['X Confidence'])
                player2Rating = Rating(playerHistory[player2]['O ELO'],playerHistory[player2]['O Confidence'])
                player1Rating, player2Rating = rate_1vs1(player1Rating, player2Rating, drawn=False)
                playerHistory[player1]['X ELO'] = player1Rating.mu
                playerHistory[player1]['X Confidence'] = player1Rating.sigma
                playerHistory[player2]['O ELO'] = player2Rating.mu
                playerHistory[player2]['O Confidence'] = player2Rating.sigma
                playerHistory[player1]['X Wins'] += 1
                playerHistory[player2]['O Losses'] += 1 
                

            else:
                print("Player 2 Wins!")
                player1Rating = Rating(playerHistory[player1]['X ELO'],playerHistory[player1]['X Confidence'])
                player2Rating = Rating(playerHistory[player2]['O ELO'],playerHistory[player2]['O Confidence'])
                player2Rating, player1Rating = rate_1vs1(player2Rating, player1Rating, drawn=False)
                playerHistory[player1]['X ELO'] = player1Rating.mu
                playerHistory[player1]['X Confidence'] = player1Rating.sigma
                playerHistory[player2]['O ELO'] = player2Rating.mu
                playerHistory[player2]['O Confidence'] = player2Rating.sigma
                playerHistory[player1]['X Losses'] += 1
                playerHistory[player2]['O Wins'] += 1 
            
        return

    #Really only applicable to human players
    else:
        print("Can't insert there!")
        position = int(input("Please enter new position:  "))
        insertLetter(position, letter, coordinates)
        return

def checkForWin(position):
    
    #check across
    for row in position:
        for i in range(4):
            if row[0+i] == row[1+i] == row[2+i] == row[3+i] and row[0+i] != " ":
                return True

    #check verical
    for i in range(len(position[0])):
        for j in range(3):
            if position[0+j][i] == position[1+j][i] == position[2+j][i] == position[3+j][i] and position[0+j][i] != " ":
                return True

    #check down diagonal
    for i in range(len(position[0])-3): #col
        for j in range(len(position)-3): #row
            if position[0+j][0+i] == position[1+j][1+i] == position[2+j][2+i] == position[3+j][3+i] and position[0+j][0+i] != " ":
                return True

    #check up diagonal
    for i in range(len(position[0])-3): #col
        for j in range(len(position)-3): #row
            if position[5-j][0+i] == position[4-j][1+i] == position[3-j][2+i] == position[2-j][3+i] and position[5-j][0+i] != " ":
                return True
    
    return False

def playerMove(position,letter):

    while 'coordinates' not in locals():
        y = int(input("Enter the column for 'O':  "))
        if y >= 0 and y < len(position[0]):
            for x in range(len(position)):
                if (position[len(position) - 1 - x][y] == ' '):
                    coordinates = (len(position) - 1 - x,y)
                    break
            
                if len(position) - 1 - x == 0:
                    print("No more spots available, please choose another column")

        else:
            print("Invalid Entry, please enter a number")
        
    insertLetter(position, letter, coordinates)
    return

currentPlayer = "X"
while not checkForWin(position) and not checkForDraw(position):
    
    if currentPlayer == "X":
        p = subprocess.run(["python",player1,json.dumps(position),"X"], capture_output=True, text=True)
        
    else:
        p = subprocess.run(["python",player2,json.dumps(position),"O"], capture_output=True, text=True)

    output = eval(p.stdout)
    insertLetter(position,currentPlayer,output)

    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

with open("playerHistory.pickle", "wb") as f:
    pickle.dump(playerHistory, f)

print(playerHistory)