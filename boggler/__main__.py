"""Boggler Demo"""
import argparse
import sys
from pathlib import Path
from .boggler_utils import BoggleBoard, build_full_boggle_tree, read_boggle_file

parser = argparse.ArgumentParser(
    prog="boggler",
    description="Boggle board game solver"
)

parser.add_argument("board", type=Path, help="Path to board CSV file")
parser.add_argument("wordlists", type=Path,
    help="Path to directory of wordlist files. The directory must contain \
        text files of the form words_X.txt where \"X\" is a character of \
        the alphabet")
parser.add_argument("max_word_length", nargs="?", type=int, default=16,
    help="Maximum length of words searched for on provided board")

args = parser.parse_args()

def main():
    """Command line tool for sovling Boggle boards"""
    board = read_boggle_file(args.board)
    try:
        boggle_board = BoggleBoard(board, args.max_word_length)
    except ValueError:
        print("Invalid MAX_WORD_LENGTH. Please try again with a valid integer.")
        sys.exit()

    try:
        boggle_tree = build_full_boggle_tree(boggle_board, args.wordlists)

        print("\nBOARD")
        print(boggle_board)

        for start_pos, tree in boggle_tree.items():
            print(f"\nStarting @ {start_pos}...")
            for word in tree.word_paths:
                print(f"{word[0]: <{boggle_board.max_word_len}}: {word[1]}")

    except ValueError:
        print("The [MAX_WORD_LENGTH] argument must be an integer.")
        print("Please try again.")
        sys.exit(1)

if __name__ == '__main__':
    main()
