from sys import argv
from random import randint
from math import sqrt

def readDiceFile(path):
    with open(path, 'r+') as f:
        # Ignore first two lines
        f.readline()
        f.readline()
        dice = []
        line = ''.join(f.readline().rstrip().split(','))
        while(line):
            dice.append(line)
            line = ''.join(f.readline().rstrip().split(','))

        return dice

def rollDie(die):
    return str(die[randint(0, len(die) - 1)])

def rollDice(dice):
    rolls = []
    for die in dice:
        roll = rollDie(die)
        rolls.append(roll)

    return rolls

if __name__ == '__main__':
    if len(argv) != 2:
        print('Usage: python3 board_randomizer DICE_FILE')
    else:
        dice = readDiceFile(argv[1])
        rolls = rollDice(dice)

        # Format dice rolls for boards file
        board_size = int(sqrt(len(rolls)))
        for i in range(0, len(dice), board_size):
            print("".join(rolls[i:i+board_size]))
