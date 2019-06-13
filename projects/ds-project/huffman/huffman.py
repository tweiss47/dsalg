# Implement Huffman encoding and decoding for text input


import sys
import heapq


class HuffNode:
    '''
    Node class for building a Huffman encoding tree.
    '''
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


def huffman_encoding(data):
    '''
    Encode the data into a string of 0/1 characters, suitable for compaction
    into an int or byte array.

    data: the string to be encoded

    Returns: a tuple of the encoded data string and the tree used to decode
    '''
    if len(data) == 0: return None, None
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
    # Build of dictionary of character frequencies
    frequency_map = dict()
    for char in data:
        count = frequency_map.get(char, 0)
        frequency_map[char] = count + 1

    # Use character frequencies to build a heap of HuffNodes
    nodes = []
    for key, value in frequency_map.items():
        heapq.heappush(nodes, HuffNode(value, key))

    # Special case when the tree has only one type of character
    if len(nodes) == 1:
        root = HuffNode(nodes[0].count)
        root.left = nodes[0]
        return root

    # Build the tree by combining nodes with the smallest count values
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


def encode_with_tree(data, root):
    '''
    Encode the input data with the Huffman tree (root)

    Returns: the data encoded as a string of 0/1 characters
    '''
    # Build a map of characters to codes from the tree rather than traversing
    # for each character
    code_map = dict()

    # recursive helper to traverse the tree
    def traverse(node, code):
        # when you hit a leaf insert the char and code into code_map
        if node.char:
            code_map[node.char] = code
            return
        if node.left:
            traverse(node.left, code + '0')
        if node.right:
            traverse(node.right, code + '1')

    # invoke the traversal
    traverse(root, '')

    # use the map to encode the data
    chars = [code_map[char] for char in data]
    return ''.join(chars)


if __name__ == '__main__':
    def is_valid_encoding(encoding):
        if not encoding or len(encoding) == 0:
            return False
        for char in encoding:
            if not (char == '0' or char == '1'):
                return False
        return True

    def data_was_compressed(data, encoded):
        size_encoded = sys.getsizeof(int(encoded, base=2))
        size_original = sys.getsizeof(data)
        return size_encoded < size_original

    print("Testing Huffman encoding")

    # Test some nominal cases
    nominal_cases = [
        "Udacity is udacious",
        "Well, everybody's heard about the bird. Bird, bird, bird",
        "The bird is the word"
    ]
    for data in nominal_cases:
        encoded, tree = huffman_encoding(data)
        assert len(encoded) > 0
        assert is_valid_encoding(encoded)
        decoded = huffman_decoding(encoded, tree)
        assert data == decoded
        assert data_was_compressed(data, encoded)
        # print(data, ":", encoded)

    # Corner cases
    data = ""
    encode, tree = huffman_encoding(data)
    assert encode is None
    assert tree is None

    data = "a"
    encode, tree = huffman_encoding(data)
    assert encode == "0"
    decoded = huffman_decoding(encode, tree)
    assert decoded == data

    data = "aaa"
    encode, tree = huffman_encoding(data)
    assert encode == "000"
    decoded = huffman_decoding(encode, tree)
    assert decoded == data

    data = "baa"
    encode, tree = huffman_encoding(data)
    assert encode == "011"
    decoded = huffman_decoding(encode, tree)
    assert decoded == data

    print("All tests passed!")

    # demonstration from the problem description
    def demo(sentence):
        print ("The size of the data is: {}\n".format(sys.getsizeof(sentence)))
        print ("The content of the data is: {}\n".format(sentence))

        encoded_data, tree = huffman_encoding(sentence)

        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)

        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the encoded data is: {}\n".format(decoded_data))

    # demo("The bird is the word")
