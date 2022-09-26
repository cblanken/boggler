'''Module to generate random Boggle boards for testing'''
from sys import argv, stderr
from random import randint, shuffle
from math import sqrt
from os import path

def read_dice_file(dice_path: str):
    '''Return list of die strings from file ignoring all comments (#)'''
    with open(path.abspath(dice_path), 'r+', encoding="utf-8") as file:
        return [line.rstrip().split(',') for line in file.readlines() if line[0] != "#"]

def roll_die(die: str):
    '''Return a face of the given die string to simulate rolling a die'''
    return str(die[randint(0, len(die) - 1)])

def roll_dice(dice: list[str]):
    '''Return a random roll for each die'''
    return [ roll_die(die) for die in dice ]

def get_random_board(dice: list[str]):
    shuffle(dice)
    rolls = roll_dice(dice)

    # Format dice rolls for boards file
    board_size = int(sqrt(len(rolls)))
    board = []
    for i in range(0, len(dice), board_size):
        board.append(rolls[i:i+board_size])
    return board

def get_random_board_csv(dice: list[str]):
    board = get_random_board(dice)
    board = [",".join(row) for row in board]
    return board

if __name__ == '__main__':
    if len(argv) != 2:
        print('Usage: python3 board_randomizer.py <dice_file>')
    else:
        try:
            dice = read_dice_file(path.abspath(argv[1]))
            board = get_random_board_csv(dice)
            for row in board:
                print(row)
        except Exception as e:
            print("Argument must be a valid file path!", file=stderr)


