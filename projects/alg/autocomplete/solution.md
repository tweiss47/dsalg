# Autocomplete with Tries

The solution for this problem is in the Jupyter Notebook `Trie.ipynb`.

Storage requirements for the Trie depend on the number of words stored (n)
and the number of characters in those words (m). If there are no shared
prefixes then there will be a number of TrieNode objects created equal to m.
So O(m) would be the upper bound for storage requirements.

`insert()` and `find()` operations require time proportional to the number of
characters in the word.

`suffixes()` in the worst case would traverse the entire Trie, O(m), and
require space proportional to the depth of the Trie for the traversal for the
runtime stack. The depth of the Trie would be equal to the longest word
inserted. In addition the method stores all the paths in a list. This will
require space proportional to the Trie itself - O(m) for m equal to the total
number of characters in all the strings stored - for the string data storage.
And the list itself will space to hold the individual strings.
