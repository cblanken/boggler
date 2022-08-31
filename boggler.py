"""Boggler Demo"""
import sys
from pathlib import Path
from boggler_utils import BoggleBoard, build_full_boggle_tree, read_boggle_file

if __name__ == '__main__':
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print('Usage: python3 boggler.py <BOARD_FILE> <WORDLISTS_DIR> [MAX_WORD_LENGTH]')
        sys.exit(1)

    b1 = read_boggle_file(Path(sys.argv[1]))
    if len(sys.argv) == 3:
        b1_board = BoggleBoard(b1)
        print(b1_board)
        boggle_tree = build_full_boggle_tree(b1_board, Path(sys.argv[2]))
    elif len(sys.argv) == 4:
        try :
            b1_board = BoggleBoard(b1, int(sys.argv[3]))
            print(b1_board)
            boggle_tree = build_full_boggle_tree(b1_board, Path(sys.argv[2]))
        except ValueError as e:
            print("The [MAX_WORD_LENGTH] argument must be an integer.")
            print("Please try again.")
            sys.exit(1)
