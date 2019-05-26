import sys
import heapq


def huffman_encoding(data):
    '''
    Encode the data into a string of 0/1 characters, suitable for compaction
    into an int or byte array.

    data: the string to be encoded

    Returns: a tuple of the encoded data string and the tree used to decode
    '''
    root = build_huffman_tree(data)
    encoded = encode_with_tree(data, root)
    return encoded, root


def huffman_decoding(data, tree):
    '''
    Decode data using the Huffman tree.

    Resturns: a string containing the decoded data
    '''
    chars = []
    # start at the top of the tree and move once for each encoded character
    node = tree
    for char in data:
        # 0 indicates the character is to the left, 1 to the right
        if char == '0':
            node = node.left
        else:
            node = node.right
        if node.char:
            # when we get to a leaf node we have decoded one character
            # save it and reset to the root of the tree
            chars.append(node.char)
            node = tree
    return ''.join(chars)


def build_huffman_tree(data):
    '''
    Build a tree that can be used to encode and decode a string using Huffman
    coding.

    Returns: the HuffNode object at the root of the tree
    '''
    frequency_map = get_character_frequency(data)
    return build_tree(frequency_map)


def encode_with_tree(data, root):
    '''
    Encode the input data with the Huffman tree (root)

    Returns: the data encoded as a string of 0/1 characters
    '''
    code_map = tree_to_code_map(root)
    return encode_string(a_great_sentence, code_map)


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


def build_tree(frequency_map):
    '''
    Build the Huffman Tree by assigning a binary code to each letter, using
    codes for the more frequent letters. (This is the heart of the
    algorithm.)
    '''
    # Use character frequencies to build a heap of HuffNodes
    nodes = []
    for key, value in frequency_map.items():
        heapq.heappush(nodes, HuffNode(value, key))

    while (len(nodes) > 1):
        # pull two nodes off the front of the heap
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)

        # create a new node with a value equal to the sum of the popped nodes
        node = HuffNode(left.count + right.count)
        node.left = left
        node.right = right

        # insert the node back into the heap
        heapq.heappush(nodes, node)
    return nodes[0]


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
    chars = []
    for char in s:
        chars.append(code_map[char])
    return ''.join(chars)


if __name__ == '__main__':
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
