'''Boggler Utils'''

from __future__ import annotations
from os import path
import sys

class BoardCell:
    '''Boggle Board cell'''
    def __init__(self, row: int, col: int, letter: str, adjacent_cells: list[BoardCell] = None) -> BoardCell:
        self.__row: int = row
        self.__col: int = col
        self.__pos: (int, int) = (self.__row, self.__col)
        self.__letter: str = letter
        self.__adjacent_cells: list[BoardCell] = adjacent_cells

    @property
    def row(self) -> int:
        '''Getter for row property'''
        return self.__row

    @property
    def col(self) -> int:
        '''Getter for col property'''
        return self.__col

    @property
    def pos(self) -> (int, int):
        '''Getter for pos property'''
        return self.__pos

    @property
    def letter(self) -> str:
        '''Getter for letter property'''
        return self.__letter

    @property
    def adjacent_cells(self) -> list[BoardCell]:
        '''Getter for adjacent_cells property'''
        return self.__adjacent_cells

    @adjacent_cells.setter
    def adjacent_cells(self, value):
        self.__adjacent_cells = value

    def __str__(self):
        return f"({self.__row}, {self.__col}): {self.__letter}"

class BoggleBoard:
    '''Boggle board structure'''
    def __init__(self, board: list[list[str]], max_word_len: int = 14) -> BoggleBoard:
        self.__height: int = len(board)
        self.__width: int = len(board[0]) if self.__height > 0 else 0
        self.__board: dict[(int, int), BoardCell] = {}

        # max word length is limited by size of the board
        self.__max_word_len = min(max_word_len, self.__width * self.__height)

        # Generate BoardCell for each position on the board
        for row in range(0, self.__height):
            for col in range(0, self.__width):
                #self.adjacency_dict[(row, col)] = self.__get_adjacent_indexes(row, col)
                self.__board[(row, col)] = BoardCell(row, col, board[row][col])

        # Update adjacent cell references for each BoardCell
        for cell in self.__board.values():
            adjacent_indexes = self.__get_adjacent_indexes(cell.row, cell.col)
            #print(cell)
            #print(adjacent_indexes)
            cell.adjacent_cells = [self.__board[(x[0], x[1])] for x in adjacent_indexes]

    @property
    def height(self) -> int:
        '''Getter for height property'''
        return self.__height

    @property
    def width(self) -> int:
        '''Getter for width property'''
        return self.__width

    @property
    def max_word_len(self) -> int:
        '''Getter for maximum word length property'''
        return self.__max_word_len

    @property
    def board(self) -> dict((int, int), BoardCell):
        '''Getter for board property'''
        return self.__board

    def __get_adjacent_indexes(self, row, col):
        '''Return adjecency list for board of size `row x col`'''
        indexes = []
        if row > 0:
            indexes.append((row-1, col)) # up
            if col > 0:
                indexes.append((row-1, col-1)) # up-left
            if col < self.width - 1:
                indexes.append((row-1, col+1)) # up-right
        if row < self.height - 1:
            indexes.append((row+1, col)) # down
            if col > 0:
                indexes.append((row+1, col-1)) # down-left
            if col < self.width - 1:
                indexes.append((row+1, col+1)) # down-right
        if col > 0:
            indexes.append((row, col-1)) # left
        if col < self.width - 1:
            indexes.append((row, col+1)) # right
        return indexes

    def get_cell(self, row: int, col: int) -> str:
        '''Return the value at the specified row x column'''
        return self.__board[(row, col)]

class WordNode:
    '''A node describing a single letter in a WordTree.'''
    def __init__(self, letter: str, is_word: bool = False, parent: WordNode = None, children: dict[WordNode] = None, board_pos = None) -> WordNode:
        self.__letter = letter
        self.__is_word = is_word
        self.__children = children if children is not None else {}
        self.__parent = parent
        self.__board_pos = board_pos

    @property
    def char(self) -> str:
        '''Getter for char property'''
        return self.__letter

    @property
    def is_word(self) -> bool:
        '''Getter for is_word property'''
        return self.__is_word
    
    @is_word.setter
    def is_word(self, value):
        self.__is_word = value

    @property
    def children(self) -> dict[WordNode]:
        '''Getter for children property'''
        return self.__children

    @property
    def parent(self) -> WordNode:
        '''Getter for parent property'''
        return self.__parent

    @property
    def board_pos(self) -> (int, int):
        '''Getter for board_pos property'''
        return self.__board_pos

    def add_child_node(self, node):
        '''Add child node to `children` dictionary, indexed by the nodes' `char`'''
        self.children[node.char] = node

    @property
    def path(self) -> list[WordNode]:
        '''Return list of nodes from current node to the root'''
        curr_node = self
        path = []
        path.append(curr_node.board_pos)
        while curr_node.parent is not None:
            path.append(curr_node.parent.board_pos)
            curr_node = curr_node.parent

        return path

    def __str__(self):
        return f"WordNode: {self.char}, {self.is_word}"

    def __repr__(self):
        return self.__str__()

class WordTree:
    '''A tree populated by WordNode(s) to complete words from a given root letter and wordlist'''
    def __init__(self, alphabet: str, root: WordNode, words: list[str] = None, max_word_len = 16) -> WordTree:
        self.__alphabet = alphabet
        self.__wordlist = words
        self.__root = root
        self.__max_word_len = max_word_len
        self.__tree = {}

        # Generate root node
        self.__tree[root.char] = root
        self.active_node: WordNode = self.__tree[root.char]

        # Populate tree from wordlist
        if words is not None:
            for word in words:
                self.__insert_word(word)

    @property
    def alphabet(self) -> str:
        '''Getter for alphabet property'''
        return self.__alphabet

    @property
    def wordlist(self) -> list[str]:
        '''Getter for wordlist property'''
        return self.__wordlist

    @property
    def root(self) -> str:
        '''Getter for root property'''
        return self.__root

    @property
    def max_word_len(self) -> int:
        '''Getter for max_word_len property'''
        return self.__max_word_len

    @property
    def tree(self) -> dict[str]:
        '''Getter for tree property'''
        return self.__tree

    def __str__(self):
        return ", ".join(self.wordlist)
    
    def insert_letter(self, letter: str, parent: WordNode, is_word: bool = False, children: dict[WordNode] = None, board_pos = None):
        '''Create WordNode for `letter` and into WordTree under `parent`'''
        node = WordNode(letter, is_word, parent, children, board_pos)
        parent.add_child_node(node)

    def __insert_word(self, word: str) -> bool:
        '''Returns True if word was inserted into the tree, otherwise False'''
        if word is None or word[0] != self.root.char:
            return False
        curr_node = self.tree[word[0]]
        for letter in word[1:self.max_word_len]:
            # Insert new WordNode for each letter that doesen't already exist in the tree
            if letter not in curr_node.children:
                self.insert_letter(letter, curr_node)
            curr_node = curr_node.children[letter]
        # Mark the last node of the word
        curr_node.is_word = len(word) <= self.max_word_len
        #print(f"Added: {word[:self.max_word_len]}")
        return True

    def search(self, word: str) -> WordNode:
        '''Return True if a given word is in the tree otherwise return False'''
        if len(word) == 0 or word is None:
            return False

        curr_node = self.tree[word[0]]
        for char in word[1:]:
            if char not in curr_node.children:
                return None

            curr_node = curr_node.children[char]

        return curr_node

    def build_boggle_tree(self, board: BoggleBoard, board_cell: BoardCell, subtree: WordTree, depth: int = 0) -> WordTree:
        '''Return subtree of board given a particular root (first letter).

        Keyword arguments:
        board       -- the board the new tree is based on
        board_node  -- a pointer on the board where new branch nodes can be inserted into the tree
        dict_node   -- a pointer on the dictionary where nodes are read from for validation
        subtree     -- the partial tree passed to the next recursive step for generating branches
        '''
        
        # TODO rework active_node refs for recursion so don't have to be reset to parent at every point of return
        if self.active_node.is_word and len(self.active_node.children) == 0:
            word_path = subtree.active_node.path[::-1]
            # print("WORD FOUND:", "".join([board.board[x].letter for x in word_path]), word_path)
            self.active_node = self.active_node.parent
            subtree.active_node = subtree.active_node.parent
            return
        elif self.active_node.is_word:
            word_path = subtree.active_node.path[::-1]
            # print("WORD FOUND:", "".join([board.board[x].letter for x in word_path]), word_path)
        elif depth > self.max_word_len:
            # print(f"MAX DEPTH REACHED! Depth = {depth}")
            self.active_node = self.active_node.parent
            subtree.active_node = subtree.active_node.parent
            return

        # Branch for each adjacent board cell
        for cell in board_cell.adjacent_cells:
            # Check dictionary and exclude nodes already in path
            if cell.letter in self.active_node.children and cell.pos not in subtree.active_node.path:
                new_node = WordNode(cell.letter, self.active_node.is_word, subtree.active_node, board_pos = cell.pos)
                subtree.active_node.add_child_node(new_node)
                subtree.active_node = subtree.active_node.children[cell.letter] # update subtree pointer
                self.active_node = self.active_node.children[cell.letter] # update dictionary tree pointer
                self.build_boggle_tree(board, board.board[cell.pos], subtree, depth=depth+1)

        # print(f"DONE SEARCHING at {subtree.active_node}")

        self.active_node = self.active_node.parent
        subtree.active_node = subtree.active_node.parent
        return subtree

def build_full_boggle_tree(board: BoggleBoard, wordlist_path: str) -> dict[str, WordTree]:
    '''Return dictionary of WordTree(s) for every letter on a BoggleBoard'''
    alphabet = "".join(sorted(set([cell.letter for cell in board.board.values()])))
    board_tree = {}
    index = {}
    
    print("Reading in wordlists...")
    # alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        filename = "words_" + letter + ".txt"
        print(f">> {letter}: {filename}")
        wordlist = read_wordlist(path.join(path.abspath(wordlist_path), filename))
        index[letter] = wordlist

    print("Generating WordTrees")
    for cell in board.board.values():
        print(cell)
        dict_tree = WordTree(alphabet, WordNode(cell.letter), index[cell.letter])
        sub_tree = WordTree(alphabet, WordNode(cell.letter, False, board_pos=cell.pos))
        board_tree[cell.pos] = dict_tree.build_boggle_tree(board, cell, sub_tree)

    return board_tree

def read_wordlist(file):
    '''Return dictionary of words with associated word count (1 by default)'''
    with open(file, 'r', encoding='utf-8') as file:
        return {k:1 for k in file.read().split()}

def read_boggle_file(file):
    '''Return list of rows from Boggle board file'''
    with open(file, 'r', encoding='utf-8') as file:
        return [x.rstrip() for x in file.readlines()]

if __name__ == "__main__":

    b2 = [
        "iats",
        "osep",
        "tras",
        "yegc"
    ]

    b2_board = BoggleBoard(b2)

    # sample_dict = read_wordlist("wordlists/dwyl/words_a.txt")
    #sample_tree = WordTree("abcdefghijklmnopqrstuvwxyz", WordNode("a"), sample_dict)
    #print("=" * 50)

    #start_pos = (0,1)
    #b2_tree = WordTree("abcdefghijklmnopqrstuvwxyz", WordNode("a", False, board_pos=start_pos))
    #sub_tree = sample_tree.build_boggle_tree(b2_board, b2_board.board[start_pos], b2_tree)

    # TODO fix dict[value] type hints to dict[key, value]

    boggle_tree = build_full_boggle_tree(b2_board, "wordlists/dwyl")
