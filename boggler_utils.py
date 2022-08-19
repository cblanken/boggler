'''Dictionary Utils'''
class WordNode:
    '''A node that indicates a single letter in a word. Used to populate a WordTree'''
    def __init__(self, char: str, is_word: bool, children: dict['WordNode'] = None) -> 'WordNode':
        self.char = char
        self.is_word = is_word
        self.children = children if children is not None else {}

    def add_child_node(self, node):
        '''Add child node to `children` dictionary, indexed by the nodes' `char`'''
        self.children[node.char] = node

    def __str__(self):
        return f"WordNode: {self.char}, {self.is_word}, {self.children}"

    def __repr__(self):
        return self.__str__()

class WordTree:
    '''A tree populated by WordNode(s) to complete words from a given wordlist'''
    def __init__(self, wordlist: list[str], alphabet: str, max_word_len: int = 16) -> WordNode:

        self.wordlist = wordlist
        self.max_word_len = max_word_len
        # Generate root nodes for each letter of the alphabet
        self.tree = {}
        for char in alphabet:
            self.tree[char] = WordNode(char, False)

        # Populate tree from wordlist
        for word in wordlist:
            self.__insert_word(word)

    def __str__(self):
        return ", ".join(self.wordlist)

    def __insert_word(self, word):
        curr_node = self.tree[word[0]]
        # print(word[0])
        for letter in word[1:self.max_word_len]:
            # Insert new WordNode for each letter that doesen't already exist in the tree
            if letter not in curr_node.children:
                curr_node.children[letter] = WordNode(letter, False)
                # print(letter)
            curr_node = curr_node.children[letter]
        # Mark the last node of the word
        curr_node.is_word = len(word) <= self.max_word_len
        print(f"Added: {word[:self.max_word_len]}")

    def search(self, word) -> bool:
        '''Return True if a given word is in the tree otherwise return False'''
        curr_node = self.tree[word[0]]
        for char in word[1:]:
            if char not in curr_node.children:
                return False

            curr_node = curr_node.children[char]

        return curr_node.is_word


if __name__ == "__main__":
    tree = WordTree(['anger',
        'ape',
        'bigger',
        'bit',
        'bite',
        'biter',
        'cart',
        'cast',
        ], "abcdefghijklmnopqrstuvwxyz")
    print(tree)
    print(tree.search('cast'))
    print(tree.search('hype'))
