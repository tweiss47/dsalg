# Autocomplete with Tries

# This is a copy of the code setup on Trie.py workbood to test out the Trie
# autocomplete functionality

## Represents a single node in the Trie
class TrieNode:
    def __init__(self, char=''):
        ## Initialize this node in the Trie
        self.children = {}
        self.is_word = False
        self.char = char # only used for debugging/__repr__()

    def insert(self, char):
        ## Add a child node in this Trie
        if char not in self.children:
            self.children[char] = TrieNode(char)

    def suffixes(self):
        # recursive function that collects the suffixes for all complete
        # words below this node
        result = []
        def traverse(node, suffix):
            if node.is_word:
                result.append(suffix)

            for char, child in node.children.items():
                traverse(child, suffix + char)

        traverse(self, "")
        return result

    def __repr__(self):
        return f"Node({self.char},{self.is_word})"


## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        node = self.root
        for char in word:
            node.insert(char)
            node = node.children[char]
        node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node


if __name__ == "__main__":
    t = Trie()
    wordList = [
        "ant", "anthology", "antagonist", "antonym",
        "fun", "function", "factory",
        "trie", "trigger", "trigonometry", "tripod"
    ]
    for word in wordList:
        t.insert(word)

    print(t.find(""))
    print(t.find("f"))
    print(t.find("fu"))
    print(t.find("fun"))
    print(t.find("funny"))

    f = t.find("f")
    print(f.suffixes())

    fu = t.find("fu")
    print(fu.suffixes())

    head = t.find("")
    print(head.suffixes())
