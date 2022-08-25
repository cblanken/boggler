'''Boggler Utils'''

from __future__ import annotations

class BoardCell:
    '''Boggle Board cell'''
    def __init__(self, row: int, col: int, letter: str, adjacent_indexes: list[list[str]]) -> BoardCell:
        self.__row = row
        self.__col = col
        self.__letter = letter
        self.__adjacent_indexes = adjacent_indexes

    @property
    def row(self) -> int:
        '''Getter for row property'''
        return self.__row

    @property
    def col(self) -> int:
        '''Getter for col property'''
        return self.__col

    @property
    def letter(self) -> str:
        '''Getter for letter property'''
        return self.__letter

    @property
    def adjacent_indexes(self) -> list[list[str]]:
        '''Getter for adjacent_indexes property'''
        return self.__row

    def __str__(self):
        return f"({self.__row}, {self.__col}: {self.__letter}. Adjacent nodes: {self.__adjacent_indexes})"

class BoggleBoard:
    '''Boggle board structure'''
    def __init__(self, board: list[list[str]], max_word_len: int = 14) -> BoggleBoard:
        self.__height: int = len(board)
        self.__width: int = len(board[0]) if self.__height > 0 else 0
        self.__max_word_len = min(max_word_len, self.__width * self.__height)   # max word length is determined by size of the board
        self.__board = {}
        for row in range(0, self.__height):
            for col in range(0, self.__width):
                #self.adjacency_dict[(row, col)] = self.__get_adjacent_indexes(row, col)
                adjacent_indexes = self.__get_adjacent_indexes(row, col)
                self.__board[(row, col)] = BoardCell(row, col, board[row][col], adjacent_indexes)

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
            if col < self.__width:
                indexes.append((row-1, col+1)) # up-right
        if row < self.__height:
            indexes.append((row+1, col)) # down
            if col > 0:
                indexes.append((row+1, col-1)) # down-left
            if col < self.__width:
                indexes.append((row+1, col+1)) # down-right
        if col > 0:
            indexes.append((row, col-1)) # left
        if col < self.__width:
            indexes.append((row, col+1)) # right
        return indexes

    def get_letter_at(self, row: int, col: int) -> str:
        '''Return the value at the specified row x column'''
        return self.__board[row][col]

class WordNode:
    '''A node that indicates a single letter in a word. Used to populate a WordTree'''
    def __init__(self, char: str, is_word: bool, parent: WordNode = None, children: dict[WordNode] = None, board_pos = None) -> WordNode:
        self.char = char
        self.is_word = is_word
        self.children = children if children is not None else {}
        self.parent = parent
        self.board_pos = board_pos

    def add_child_node(self, node):
        '''Add child node to `children` dictionary, indexed by the nodes' `char`'''
        self.children[node.char] = node

    def __str__(self):
        return f"WordNode: {self.char}, {self.is_word}, {self.children}"

    def __repr__(self):
        return self.__str__()

class WordTree:
    '''A tree populated by WordNode(s) to complete words from a given root letter and wordlist'''
    def __init__(self, alphabet: str, root: str, words: list[str] = None, max_word_len = 16) -> WordTree:
        self.alphabet = alphabet
        self.wordlist = words
        self.root = root
        self.active_node: WordNode = None
        self.max_word_len = max_word_len
        self.tree = {}

        # Generate root node
        self.tree[root] = WordNode(root, False)

        # Populate tree from wordlist
        for word in words:
            self.__insert_word(word)

    def __str__(self):
        return ", ".join(self.wordlist)

    def insert_letter(self, letter: str, parent: WordNode):
        '''Create WordNode for `letter` and into WordTree under `parent`'''
        parent.children[letter] = WordNode(letter, False, parent)

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

    def search(self, word: str) -> bool:
        '''Return True if a given word is in the tree otherwise return False'''
        if len(word) == 0 or word is None:
            return False

        curr_node = self.tree[word[0]]
        for char in word[1:]:
            if char not in curr_node.children:
                return False

            curr_node = curr_node.children[char]

        return curr_node.is_word

    def generate_board_sub_tree(self, boggle_board: BoggleBoard, start_cell: BoardCell) -> WordTree:
        '''Return subtree of board given a particular root (first letter)'''

        if start_cell.letter != self.root:
            print("ERROR: the start_cell and WordTree root must match!")
            return None

        sub_tree = WordTree(self.alphabet, self.root)
        root = self.root
        used_nodes = {}

        sub_tree.active_node = start_cell
        dict_ptr = self.tree[root]
        # Build WordTree to max depth
        for _ in range(0, min(boggle_board.max_word_len, self.max_word_len)):
            adjacent_letters = [boggle_board.board[pos] for pos in sub_tree.active_node.adjacent_indexes]
            for pos in sub_tree.active_node.adjacent_indexes:
                letter = boggle_board.board[pos]
                if pos not in used_nodes and letter in dict_ptr.children:
                    sub_tree.insert_letter(letter, sub_tree.active_node)
                    #sub_tree.active_node.children[letter] = dict_ptr.children[letter]

                    # TODO: find way to track used_nodes to avoid loops
                    # either check the word path by recursing up via the parents
                    # or pass it along, probably rework WordNode or BoardCell or make
                    # an intermediate object
                    # used_nodes

        return sub_tree


if __name__ == "__main__":
    sample_dict = [
        'aero',
        'anger',
        'ant',
        'ape',
        'argue',
        'ash',
        'assuage',
        'aunt',
        'auspice',
        'bigger',
        'bit',
        'bite',
        'biter',
        'cart',
        'cast',
    ]

    tree = WordTree("abcdefghijklmnopqrstuvwxyz", "a", sample_dict)
    print(tree.search('anger'))
    print(tree.search('argues'))

    b1 = [
        "aucd",
        "eegh",
        "hios",
        "trea"
    ]

    b1_board = BoggleBoard(b1)
    sub_tree = tree.generate_board_sub_tree(b1_board, b1_board.board[(3, 3)])
    print(sub_tree.search("anger"))
