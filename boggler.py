import sys
from dictionary_utils import WordTree
from copy import deepcopy

def read_boggle_file(file):
    '''Return list of rows from Boggle board file'''
    with open(file, 'r', encoding='utf-8') as file:
        return [x.rstrip() for x in file.readlines()]

def read_wordlist(file):
    '''Return dictionary of words with associated word count (1 by default)'''
    with open(file, 'r', encoding='utf-8') as file:
        return {k:1 for k in file.read().split()}
        
def get_adjacent_indexes(board, row, col):
    '''Return adjecency list for matrix (Boggle board) of size `row x col`'''
    max_height = len(board) - 1
    max_width = len(board[0]) - 1
    indexes = []
    if row > 0:
        indexes.append((row-1, col)) # up
        if col > 0:
            indexes.append((row-1, col-1)) # up-left
        if col < max_width:
            indexes.append((row-1, col+1)) # up-right
    if row < max_height:
        indexes.append((row+1, col)) # down
        if col > 0:
            indexes.append((row+1, col-1)) # down-left
        if col < max_width:
            indexes.append((row+1, col+1)) # down-right
    if col > 0:
        indexes.append((row, col-1)) # left
    if col < max_width:
        indexes.append((row, col+1)) # right

    return indexes

def find_words_by_index(board, wordlist, row, col, depth, adjacent_indexes, prefix = '', path = [], found_words = {}, prefixes = None, max_depth = 5, prefix_len = 0):
    if depth == max_depth:
        return {}

    if prefixes != None and depth == prefix_len and prefix not in prefixes:
        return {}
    prefix = prefix + board[row][col]

    found_words = deepcopy(found_words)
    path = deepcopy(path)

    path.append((row, col))
    if prefix in wordlist:
        found_words[prefix] = 1

    adjacents = [x for x in adjacent_indexes[(row, col)] if x not in path]
    for adj in adjacents:
        new_words = find_words_by_index(board,
                                     wordlist,
                                     adj[0],
                                     adj[1],
                                     depth+1,
                                     adjacent_indexes,
                                     prefix,
                                     path,
                                     found_words,
                                     prefixes,
                                     max_depth,
                                     prefix_len)
        for k, v in new_words.items():
            if k in wordlist and k in found_words:
                # Add and increment word counts
                #foundWords[k] = foundWords[k] + v
                found_words[k] = found_words[k]
            elif k in wordlist.keys():
                found_words[k] = v

    return found_words

def find_words(board, adjacent_indexes,  wordlist_path, max_depth = 5, prefixes = None, prefix_len = 0):
    words = {}
    for row in range(len(board)):
        for col in range(len(board[0])):
            # Find words for each row/col starting points
            wordlist = read_wordlist(wordlist_path + 'words_' + board[row][col] + '.txt')
            newWords = find_words_by_index(board, wordlist, row, col, 0, adjacent_indexes, prefixes = prefixes, max_depth = max_depth, prefix_len = prefix_len)
            for w,v in newWords.items():
                # Add and increment word counts
                words[w] = words[w] + v if w in words.keys() else v

    return words


if __name__ == '__main__':
    if len(sys.argv) != 5:
        print('Usage: python3 blogger.py <BOARD_FILE> <MAX_WORD_LENGTH> <PREFIX_FILE> <WORDLISTS>')
    else:
        board = read_boggle_file(sys.argv[1])
        print(board)
        adjacentIndexes = {}
        for r in range(len(board)):
            for c in range(len(board)):
                adjacentIndexes[(r,c)] = get_adjacent_indexes(board, r, c)

        adjacentLetters = {
            k:[board[pos[0]][pos[1]] for pos in v] for (k,v) in adjacentIndexes.items()
        }

        maxSize = int(sys.argv[2], 10)
        prefixes = read_wordlist(sys.argv[3])
        words = find_words(board, adjacentIndexes, sys.argv[4], maxSize, prefixes, 4)
        for w in words:
            print(w)
