'''Boggler Utils'''

from __future__ import annotations
from multiprocessing import Pool

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
        return f"({self.__row}, {self.__col}: {self.__letter} | {self.__adjacent_cells})"

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
    def __init__(self, char: str, is_word: bool, parent: WordNode = None, children: dict[WordNode] = None, board_pos = None) -> WordNode:
        self.char = char
        self.is_word = is_word
        self.children = children if children is not None else {}
        self.parent = parent
        self.board_pos = board_pos

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
        # return f"WordNode: {self.char}, {self.is_word}, {self.children}"
        return f"WordNode: {self.char}, {self.is_word}"

    def __repr__(self):
        return self.__str__()

class WordTree:
    '''A tree populated by WordNode(s) to complete words from a given root letter and wordlist'''
    def __init__(self, alphabet: str, root: str, words: list[str] = None, max_word_len = 16) -> WordTree:
        self.alphabet = alphabet
        self.wordlist = words
        self.root = root
        self.max_word_len = max_word_len
        self.tree = {}

        # Generate root node
        self.tree[root] = WordNode(root, False)
        self.active_node: WordNode = self.tree[root]

        # Populate tree from wordlist
        if words is not None:
            for word in words:
                self.__insert_word(word)


    def __str__(self):
        return ", ".join(self.wordlist)

    def insert_letter(self, letter: str, parent: WordNode, is_word: bool = False, children: dict[WordNode] = None, board_pos = None):
        '''Create WordNode for `letter` and into WordTree under `parent`'''
        node = WordNode(letter, is_word, parent, children, board_pos)
        parent.add_child_node(node)

    def __insert_word(self, word: str) -> bool:
        '''Returns True if word was inserted into the tree, otherwise False'''
        if word is None or word[0] != self.root:
            return False
        curr_node = self.tree[word[0]]
        # print(word[0])
        for letter in word[1:self.max_word_len]:
            # Insert new WordNode for each letter that doesen't already exist in the tree
            if letter not in curr_node.children:
                self.insert_letter(letter, curr_node)
                # print(letter)
            curr_node = curr_node.children[letter]
        # Mark the last node of the word
        curr_node.is_word = len(word) <= self.max_word_len
        print(f"Added: {word[:self.max_word_len]}")
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
            print("WORD FOUND:", "".join([board.board[x].letter for x in word_path]), word_path)
            self.active_node = self.active_node.parent
            subtree.active_node = subtree.active_node.parent
            return
        elif self.active_node.is_word:
            word_path = subtree.active_node.path[::-1]
            print("WORD FOUND:", "".join([board.board[x].letter for x in word_path]), word_path)
        elif depth > self.max_word_len:
            print(f"MAX DEPTH REACHED! Depth = {depth}")
            self.active_node = self.active_node.parent
            subtree.active_node = subtree.active_node.parent
            return

        # Branch for each adjacent board cell
        for cell in board_cell.adjacent_cells:
            # Check dictionary and exclude nodes already in path
            print("Cell:", cell.letter, cell.pos, subtree.active_node.path)
            if cell.letter in self.active_node.children and cell.pos not in subtree.active_node.path:
                # print(cell)
                print(self.active_node)
                #subtree.insert_letter(cell.letter, subtree.active_node, self.active_node.is_word, board_pos=cell.pos)
                new_node = WordNode(cell.letter, self.active_node.is_word, subtree.active_node, board_pos = cell.pos)
                subtree.active_node.add_child_node(new_node)
                subtree.active_node = subtree.active_node.children[cell.letter] # update subtree pointer
                self.active_node = self.active_node.children[cell.letter] # update dictionary tree pointer
                self.build_boggle_tree(board, board.board[cell.pos], subtree)

        print(f"DONE SEARCHING at {subtree.active_node}")

        self.active_node = self.active_node.parent
        subtree.active_node = subtree.active_node.parent
        return subtree

def read_wordlist(file):
    '''Return dictionary of words with associated word count (1 by default)'''
    with open(file, 'r', encoding='utf-8') as file:
        return {k:1 for k in file.read().split()}


if __name__ == "__main__":
    # sample_dict = [
    #     'aero',
    #     'anger',
    #     'ant',
    #     'ape',
    #     'argue',
    #     'ash',
    #     'assuage',
    #     'aunt',
    #     'auspice',
    #     'bigger',
    #     'bit',
    #     'bite',
    #     'biter',
    #     'cart',
    #     'cast',
    # ]

    sample_dict = read_wordlist("wordlists/dwyl/words_a.txt")

    tree = WordTree("abcdefghijklmnopqrstuvwxyz", "a", sample_dict)
    n1 = tree.search('anger')
    #print(n1.path)
    #print(tree.search('argues'))
    print("=" * 50)

    b1 = [
        "aucd",
        "eegh",
        "hios",
        "trea"
    ]

    b2 = [
        "iats",
        "osep",
        "tras",
        "yegc"
    ]

    b1_board = BoggleBoard(b1)
    b2_board = BoggleBoard(b2)

    b1_tree = WordTree("abcdefghijklmnopqrstuvwxyz", "a")
    b1_tree.tree["a"].board_pos = (3,3)

    b2_tree = WordTree("abcdefghijklmnopqrstuvwxyz", "a")
    b2_tree.tree["a"].board_pos = (0,1)

    #sub_tree = tree.build_boggle_tree(b1_board, b1_board.board[(0,0)], b1_tree)
    sub_tree = tree.build_boggle_tree(b2_board, b2_board.board[(2,2)], b2_tree)
    #sub_tree = tree.build_board_sub_tree(b1_board, b1_board.board[(3, 3)])
    #print(sub_tree.search("anger"))
