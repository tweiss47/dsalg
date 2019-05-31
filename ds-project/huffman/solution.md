# Huffman Coding Solution

The solution for the Huffman Coding problem is contained in the `huffman.py`
file. The interface is the huffman_encoding() function which takes the data
to be encoded and outputs the encoded string and the tree which can be used
to decode the data. And the huffman_decoding() function which takes the
encoded data and the tree and returns the decoded data.

There is a class `HuffNode` used to build the encoding/decoding tree. And a
couple of helper functions.

## Design and Runtime

The encoding logic works by first building the encoding tree. And then using
the tree to encode the data.

The `build_huffman_tree()` helper starts by using a dictionary to count
character frequencies. This will take O(n) where n is the size of the string.
To sort the frequency counts the and enable easy removal of the lowest
frequency items, the heapq library is used. Building the inital heap will be
O(klog(k)) where k is the number of unique characters in the string. The tree
is then built by pulling of the smallest two nodes from the heap O(log(k))
combining them under a parent node and then inserting the result back into
the heap O(log(k)). Assuming the string contains all unique characters (the
worst case for the tree building operation) we'd expect the runtime to be
O(nlog(n)).

The `encode_with_tree()` helper does the encoding. It uses a dictionary that
maps the character to its code to avoid traversing the tree for each
character. Building the dictionary requires a complete tree traversal. O(n)
where n is the number of nodes in the tree. After that the string can be
encoded by traversing the input and doing one O(1) lookup per character.

The decoding logic in `huffman_decoding()` is a step by step traversal of the
tree, one move for each bit in the encoded data. So the runtime would be O(n)
where n is the length of the encoded data.
