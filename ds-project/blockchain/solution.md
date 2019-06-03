# Blockchain solution

The blockchain project was just to implement a blockchain. But it wasn't
entirely clear what the functional requirements were beyond keeping a chain
of blocks. So I added a method `BlockChain.is_valied()` to try to confirm the
validity of chain by checking the stored hashes against hashes of the current
data.

Otherwise the user of the BlockChain class calls `record()` to create a new
data record. Adding records is a constant time operation on the size of the
chain, but will depend on the amount of data stored in the `Block`. Checking
the validity of the chain requires traversing the chain: O(n) where n is the
number of blocks and recomputing hashes for each block.
