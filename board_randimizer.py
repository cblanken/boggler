#!/bin/python
from sys import argv
from random import randint, shuffle
from math import sqrt

def read_dice_file(path):
    with open(path, 'r+', encoding="utf-8") as file:
        # Ignore first two lines
        file.readline()
        file.readline()
        dice = []
        line = ''.join(file.readline().rstrip().split(','))
        while(line):
            dice.append(line)
            line = ''.join(file.readline().rstrip().split(','))

        return dice

def roll_die(die):
    return str(die[randint(0, len(die) - 1)])

def roll_dice(dice):
    rolls = []
    for die in dice:
        roll = roll_die(die)
        rolls.append(roll)

    return rolls

if __name__ == '__main__':
    if len(argv) != 2:
        print('Usage: python3 <board_randomizer.py> <dice_file>')
    else:
        dice = read_dice_file(argv[1])
        shuffle(dice) 
        rolls = roll_dice(dice)

        # Format dice rolls for boards file
        board_size = int(sqrt(len(rolls)))
        for i in range(0, len(dice), board_size):
            print("".join(rolls[i:i+board_size]))
