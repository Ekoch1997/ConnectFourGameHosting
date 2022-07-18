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

def compMove(position):
    moves = []
    for y in range(len(position[0])):
        for x in range(len(position)):
            if (position[len(position) - 1 - x][y] == ' '):
                moves.append((len(position) - 1 - x,y))
                break
    move = moves[randint(0,len(moves)-1)]
    print(str(move))
    return

move = compMove(position)