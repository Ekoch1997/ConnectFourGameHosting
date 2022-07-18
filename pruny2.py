from random import randint
from math import inf
import sys
import json



#Initialize Game

if sys.argv[1]:
    position = json.loads(sys.argv[1])
else:
    print("Position Available")
    position = [
        [" ", " ", " "," ", " ", " "," "],
        [" ", " ", " "," ", " ", " "," "],
        [" ", " ", " "," ", " ", " "," "],
        [" ", " ", " "," ", " ", " "," "],
        [" ", " ", " "," ", " ", " "," "],
        [" ", " ", " "," ", " ", " "," "]
    ]

player = "X"
opponent = "O"
if sys.argv[2]:
    if sys.argv[2] == "X":
        player = "X"
        opponent = "O"
    else:
        player = "O"
        opponent = "X"

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

def checkWhichMarkWon(position, mark):
    #check across
    for row in position:
        for i in range(4):
            if row[0+i] == row[1+i] == row[2+i] == row[3+i] and row[0+i] == mark:
                return True

    #check verical
    for i in range(len(position[0])):
        for j in range(3):
            if position[0+j][i] == position[1+j][i] == position[2+j][i] == position[3+j][i] and position[0+j][i] == mark:
                return True

    #check down diagonal
    for i in range(len(position[0])-3): #col
        for j in range(len(position)-3): #row
            if position[0+j][0+i] == position[1+j][1+i] == position[2+j][2+i] == position[3+j][3+i] and position[0+j][0+i] == mark:
                return True

    #check up diagonal
    for i in range(len(position[0])-3): #col
        for j in range(len(position)-3): #row
            if position[5-j][0+i] == position[4-j][1+i] == position[3-j][2+i] == position[2-j][3+i] and position[5-j][0+i] == mark:
                return True
    
    return False

def checkForDraw(position):
    #check if spots available
    for row in position:
        for val in row:
            if val == " ":
                return False
    return True

def getScore(position, player):

    if player == "X":
        opponent = "O"
    else:
        opponent = "X"
    score = 0

    #check across
    for row in position:
        for i in range(4):
            if row[0+i] != opponent and row[1+i] != opponent and row[2+i] != opponent and row[3+i] != opponent: #Possible way to win for X
                NumberInARow = 0
                if row[0+i] == player: NumberInARow += 1
                if row[1+i] == player: NumberInARow += 1
                if row[2+i] == player: NumberInARow += 1
                if row[3+i] == player: NumberInARow += 1
                score += NumberInARow * NumberInARow

            if row[0+i] != player and row[1+i] != player and row[2+i] != player and row[3+i] != player: #Possible way to win for O
                NumberInARow = 0
                if row[0+i] == opponent: NumberInARow += 1
                if row[1+i] == opponent: NumberInARow += 1
                if row[2+i] == opponent: NumberInARow += 1
                if row[3+i] == opponent: NumberInARow += 1
                score -= NumberInARow * NumberInARow

    #check verical
    for i in range(len(position[0])):
        for j in range(3):
            if position[0+j][i] != opponent and position[1+j][i] != opponent and position[2+j][i] != opponent and position[3+j][i] != opponent:
                NumberInARow = 0
                if position[0+j][i] == player: NumberInARow += 1
                if position[1+j][i] == player: NumberInARow += 1
                if position[2+j][i] == player: NumberInARow += 1
                if position[3+j][i] == player: NumberInARow += 1
                score += NumberInARow * NumberInARow
            if position[0+j][i] != player and position[1+j][i] != player and position[2+j][i] != player and position[3+j][i] != player:
                NumberInARow = 0
                if position[0+j][i] == opponent: NumberInARow += 1
                if position[1+j][i] == opponent: NumberInARow += 1
                if position[2+j][i] == opponent: NumberInARow += 1
                if position[3+j][i] == opponent: NumberInARow += 1
                score -= NumberInARow * NumberInARow

    #check down diagonal
    for i in range(len(position[0])-3): #col
        for j in range(len(position)-3): #row
            if position[0+j][0+i] != opponent and position[1+j][1+i] != opponent and position[2+j][2+i] != opponent and position[3+j][3+i] != opponent:
                NumberInARow = 0
                if position[0+j][0+i] == player: NumberInARow += 1
                if position[1+j][1+i] == player: NumberInARow += 1
                if position[2+j][2+i] == player: NumberInARow += 1
                if position[3+j][3+i] == player: NumberInARow += 1
                score += NumberInARow * NumberInARow

    #check up diagonal
    for i in range(len(position[0])-3): #col
        for j in range(len(position)-3): #row
            if position[5-j][0+i] != player and position[4-j][1+i] != player and position[3-j][2+i] != player and position[2-j][3+i] != player:
                NumberInARow = 0
                if position[5-j][0+i] == opponent: NumberInARow += 1
                if position[4-j][1+i] == opponent: NumberInARow += 1
                if position[3+j][2+i] == opponent: NumberInARow += 1
                if position[2+j][3+i] == opponent: NumberInARow += 1
                score -= NumberInARow * NumberInARow
    return score



def minimax(board, depth, alpha, beta, isMaximizing):

    if (checkWhichMarkWon(position, player)):
        return 500 - depth
    elif (checkWhichMarkWon(position, opponent)):
        return -500 + depth
    elif (checkForDraw(position)):
        return 0

    elif depth == 4:
        score = getScore(position, player)
        if isMaximizing: #opponent just moved
            return -score
        else: #comp just moved
            return score

    if (isMaximizing):
        bestScore = -inf
        for y in range(len(position[0])):
            for x in range(len(position)):
                if (position[len(position) - 1 - x][y] == ' '):
                    position[len(position) - 1 - x][y] = player
                    score = minimax(board, depth + 1, alpha, beta, False)
                    position[len(position) - 1 - x][y] = ' '
                    if (score > bestScore):
                        bestScore = score
                    if bestScore >= beta:
                        return bestScore
                    alpha = max(alpha, bestScore)

                    break #break out of column
        return bestScore

    else:
        bestScore = inf
        for y in range(len(position[0])):
            for x in range(len(position)):
                if (position[len(position) - 1 - x][y] == ' '):
                    position[len(position) - 1 - x][y] = opponent
                    score = minimax(board, depth + 1, alpha, beta, True)
                    position[len(position) - 1 - x][y] = ' '
                    if (score < bestScore):
                        bestScore = score
                    if bestScore <= alpha:
                        return bestScore
                    beta = min(beta, bestScore)

                    break #break out of column
        return bestScore

def compMove(position):
    bestScore = -inf
    bestMoves = []
    for y in range(len(position[0])):
        for x in range(len(position)):
            if (position[len(position) - 1 - x][y] == ' '):
                position[len(position) - 1 - x][y] = player
                score = minimax(position, 0, -inf, inf, False)
                position[len(position) - 1 - x][y] = ' '
                if (score > bestScore):
                    bestScore = score
                    bestMoves = []
                    bestMoves.append((len(position) - 1 - x,y))
                elif (score == bestScore):
                    bestMoves.append((len(position) - 1 - x,y))
                break #break out of column

    bestMove = bestMoves[randint(0,len(bestMoves)-1)]
    #print("Best Move Yielded: " + str(bestScore) + " Points")
    print(str(bestMove))
    return

move = compMove(position)