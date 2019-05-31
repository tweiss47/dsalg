import hashlib
import datetime


class Block:
    def __init__(self, data, next):
        """
        Each block in the chain has a timestamp, some data, a hash value and
        the hash and a link to the next block in the chain.
        """
        self.timestamp = str(datetime.datetime.utcnow()).encode("UTF-8")
        self.data = data.encode("UTF-8")
        self.next_hash = next.hash.encode("UTF-8") if next else "".encode("UTF-8")
        self.hash = self.calc_hash()
        self.next = next

    def calc_hash(self):
        """
        Compute the hash code for this block
        """
        sha = hashlib.sha256()

        sha.update(self.timestamp)
        sha.update(self.data)
        sha.update(self.next_hash)

        return sha.hexdigest()

    def __repr__(self):
        return f'Block({self.timestamp},{self.data},{self.hash})'


class BlockChain:
    def __init__(self):
        """
        The block chain starts with a dummy block. So that all data
        containing blocks have a proper reference to the adjoining block in
        the chain.
        """
        self.head = Block("Head", None)
        self.head_hash = self.head.hash

    def record(self, data):
        """
        Record the transaction described by the data parameter in the chain
        """
        self.head = Block(data, self.head)
        self.head_hash = self.head.hash

    def is_valid(self):
        """
        Seems like the minimum additional functionality that should be provided.
        Return True of each block and data in the chain returns the expected hash.
        """
        expected_hash = self.head_hash
        node = self.head
        while node:
            # compute the hash for the current node
            current_hash = node.calc_hash()
            # if it doesn't match what we expected from the previous node or
            # what was recorded when the node was created the chain is not valid
            if node.hash != expected_hash or node.hash != current_hash:
                print("Chain is invalid:")
                print(" ", node)
                print("  expected", expected_hash, type(expected_hash))
                print("  current_hash", current_hash, type(current_hash))
                return False

            # next_hash is encoded
            expected_hash = node.next_hash.decode("UTF-8")
            node = node.next

        return True


if __name__ == "__main__":
    print("Testing the blockchain")

    # Verify what one block looks like
    block = Block("Some data", None)
    print(block)

    # Add data and validate that the chain is good
    chain = BlockChain()
    assert chain.is_valid()

    chain.record("This is something to record")
    assert chain.is_valid()

    chain.record("This is something else to record")
    # save the current block for later
    block = chain.head
    assert chain.is_valid()

    chain.record("I love blockchains, they are both blocky and chainy")
    assert chain.is_valid()

    # Modify the block and then test the chain
    print(block)
    block.data = "Modified!".encode()
    assert not chain.is_valid()
    print(block)

    print("All tests pass!")


