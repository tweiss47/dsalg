import sys
import bisect

def get_character_frequency(s):
    '''
    Take a string (s) and determine the relevant frequencies of the
    characters

    Returns:
        map of character frequencies {'a': 1, 'h': 1}
    '''
    result = dict()
    for c in s:
        count = result.get(c, 0)
        result[c] = count + 1
    return result


def frequency_to_tuples(frequencies):
    '''
    Build and sort a list of tuples from lowest to highest frequencies.

    Returns:
        an ordered list of tuples (frequence, character)
    '''
    result = [HuffNode(value, key) for key, value in frequencies.items()]
    return sorted(result)


class HuffNode:
    def __init__(self, count, char=None):
        self.count = count
        self.char = char
        self.left = None
        self.right = None

    # override the rich comparison methods so we can sort our nodes during tree
    # building
    def __eq__(self, other):
        return self.count.__eq__(other.count)

    def __ne__(self, other):
        return self.count.__ne__(other.count)

    def __lt__(self, other):
        return self.count.__lt__(other.count)

    def __le__(self, other):
        return self.count.__le__(other.count)

    def __gt__(self, other):
        return self.count.__gt__(other.count)

    def __ge__(self, other):
        return self.count.__ge__(other.count)

    def __repr__(self):
        return f'Node({self.count},{self.char})'


def tuples_to_tree(tuples):
    '''
    Build the Huffman Tree by assigning a binary code to each letter, using
    codes for the more frequent letters. (This is the heart of the
    algorithm.)
    '''

    while (len(tuples) > 1):
        # pull two nodes off the front of the list
        left = tuples.pop(0)
        right = tuples.pop(0)

        # create a new node with a count value equal to the sum of the two nodes
        root = HuffNode(left.count + right.count)
        root.left = left
        root.right = right

        # insert the root into the tuple list
        index = bisect.bisect(tuples, root)
        tuples.insert(index, root)
    return tuples[0]


def tree_to_code_map(root):
    '''
    Build a map of the character to code strings
    '''
    # traverse the tree when you hit a leaf insert the char and code into a map
    code_map = dict()
    def traverse(node, code):
        if node.char:
            code_map[node.char] = code
            return
        if node.left:
            traverse(node.left, code + '0')
        if node.right:
            traverse(node.right, code + '1')

    traverse(root, '')
    return code_map


def encode_string(s, code_map):
    result = ''
    for char in s:
        result += code_map[char]
    return result


def decode_string(encoded, tree):
    result = ''
    node = tree
    for char in encoded:
        if char == '0':
            node = node.left
        else:
            node = node.right
        if node.char:
            result += node.char
            node = tree
    return result



if __name__ == '__main__':
    # a_great_sentence = "The bird is the word"
    a_great_sentence = "aaaaaaaaaaaaabc"
    frequencies = get_character_frequency(a_great_sentence)
    tuples = frequency_to_tuples(frequencies)
    print(tuples)

    print()
    root = tuples_to_tree(tuples)
    code_map = tree_to_code_map(root)
    print(code_map)

    encoded = encode_string(a_great_sentence, code_map)
    print(encoded)
    decoded = decode_string(encoded, root)
    print(decoded)


# Build the Huffman Tree by assigning a binary code to each letter, using
# codes for the more frequent letters. (This is the heart of the
# algorithm.)

# Trim the Huffman Tree (remove the frequencies from the previously built tree).

# Encode the text into its compressed form.

# Decode the text from its compressed form.

# You then will need to create encoding, decoding, and sizing schemas.
