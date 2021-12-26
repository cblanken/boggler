import sys
from copy import deepcopy

WORDLISTS_PATH = './wordlists/all/'

def readBoggleFile(file):
    with open(file, 'r') as f:
        return [x.rstrip() for x in f.readlines()]

def readWordlist(file):
    with open(file, 'r') as f:
        return {k:0 for k in f.read().split()}
        
def getAdjacentIndexes(board, row, col):
    maxHeight = len(board) - 1
    maxWidth = len(board[0]) - 1
    indexes = []
    if row > 0:
        indexes.append((row-1, col)) # up
        if col > 0:
            indexes.append((row-1, col-1)) # up-left
        if col < maxWidth:
            indexes.append((row-1, col+1)) # up-right
    if row < maxWidth:
        indexes.append((row+1, col)) # down
        if col > 0:
            indexes.append((row+1, col-1)) # down-left
        if col < maxWidth:
            indexes.append((row+1, col+1)) # down-right
    if col > 0:
        indexes.append((row, col-1)) # left
    if col < maxWidth:
        indexes.append((row, col+1)) # right

    return indexes 

def findWordsByIndex(board, wordlist, row, col, depth, adjacentIndexes, prefix = '', path = [], foundWords = {}):
    if depth == 0:
        return {}

    foundWords = deepcopy(foundWords)
    path = deepcopy(path)

    prefix = prefix + board[row][col]
    path.append((row, col))
    if prefix in wordlist:
        foundWords[prefix] = 1

    adjacents = [x for x in adjacentIndexes[(row, col)] if x not in path]
    #print('adj:', adjacents, 'p:', (row,col), 'pre:', prefix)
    for a in adjacents:
        newWords = findWordsByIndex(board, wordlist, a[0], a[1], depth-1, adjacentIndexes, prefix, path, foundWords)
        for k,v in newWords.items():
            if k in wordlist and k in foundWords:
                # Add and increment word counts
                #foundWords[k] = foundWords[k] + v
                foundWords[k] = foundWords[k]
            elif k in wordlist.keys():
                foundWords[k] = v

    return foundWords

def findWords(board, adjacentIndexes, maxDepth = 5):
    words = {}
    for row in range(len(board)):
        for col in range(len(board[0])):
            # Find words for each row/col starting points
            wordlist = readWordlist(WORDLISTS_PATH + 'words_' + board[row][col] + '.txt')
            newWords = findWordsByIndex(board, wordlist, row, col, maxDepth, adjacentIndexes)
            for w,v in newWords.items():
                # Add and increment word counts
                words[w] = words[w] + v if w in words.keys() else v

    return words


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 blogger.py boggle_board_file.txt')
    else:
        board = readBoggleFile(sys.argv[1])
        print(board)
        adjacentIndexes = {}
        for r in range(len(board)):
            for c in range(len(board)):
                adjacentIndexes[(r,c)] = getAdjacentIndexes(board, r, c)


        adjacentLetters = {k:[board[pos[0]][pos[1]] for pos in v] for (k,v) in adjacentIndexes.items()}


        maxSize = 8
        words = findWords(board, adjacentIndexes, maxSize)
        words = [w for w in words if len(w) > 2]
        for w in words:
            print(w)
        #print([w for w in words if len(w) == 3])

