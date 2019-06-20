# HTTPRouter using a Trie

The solution is implemented in `routher.py` by the `Router` and `RouteTrie`
classes. The `Router` class is just a thin wrapper over the `RouteTrie` and
just handles the not found functionality.

The runtime complexity of the trie depends on the size of the input path.
Both the `insert()` and `find()` operations both call an internal method to
first parse the string and then clean up empty the path segments. Parsing
the string would be an O(n) operation where n is number of characters and
then O(m) where m is the number of path segments. The remainder of both
algorithms will then iterate over the path segments O(m) to find or insert
the path in the trie.

The space complexity of the trie will be determined by the number of non
overlapping path segments in all the paths added, plus the total storage
required for the handlers. Each handler is only stored in the terminal
node in the trie.

The implementation will require that paths start with a /, but will treat
a completely empty path as pointing to the root. Terminal and extra /
characters the path are ignored. Passing in a new handler for an existing
path will update the handler.
