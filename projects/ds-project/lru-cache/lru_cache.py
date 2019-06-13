'''Implement a cache which has a fixed capacity and will eject entries in LRU
(Least Recently Used) order. get and set should operate in constant time.
'''


from linked_list import DList, DNode


class LRUCache:
    def __init__(self, capacity=1000):
        self.store = DList()
        self.index = dict()
        self.capacity = capacity

    def get(self, key):
        '''Retrieve the cached item stored with key. Return None if not
        available.
        '''
        # if the item is found in the index get the cache entry
        entry = self.index.get(key)
        if not entry:
            return entry

        # move the entry to the front of the cache
        self.store.remove_node(entry)
        self.store.insert_head(entry)

        # return the value
        return entry.data[1]

    def set(self, key, value):
        '''Set the value for the key. If the cache is at capacity, remove the
        LRU item.
        '''
        if key in self.index:
            # Entry is already in the cache. Update the value.
            entry = self.index[key]
            entry.data = (key, value)
            # Move it to the front of the cache store.
            self.store.remove_node(entry)
            self.store.insert_head(entry)
        else:
            # This is a new entry. Make sure there is space.
            self._ensure_capacity()

            # create a new data entry and add to the cache
            entry = DNode((key, value))
            self.store.insert_head(entry)

            # store the data entry in the index under the key
            self.index[key] = entry

    def _ensure_capacity(self):
        # If we are over the capacity limit remove items at the back of the
        # store
        count = len(self.index)
        while count >= self.capacity:
            entry = self.store.remove_tail()
            del self.index[entry.data[0]]
            count -= 1


if __name__ == '__main__':
    print('Testhing LRUCache')
    cache = LRUCache(capacity=5)
    assert(len(cache.index) == 0)

    cache.set(100, "one hundred")
    cache.set(200, "two hundred")
    cache.set(300, "three hundred")
    assert(len(cache.index) == 3)

    # get a non existant value
    assert cache.get(47) == None

    # validate that accessing a value moves it to the front of the store
    assert cache.store.tail.data[0] == 100
    assert cache.store.tail.data[1] == "one hundred"
    value = cache.get(100)
    assert value == "one hundred"
    assert cache.store.head.data[0] == 100
    assert cache.store.head.data[1] == "one hundred"

    # validate updating a value works and moves it to the front of the store
    value = cache.get(200)
    assert value == "two hundred"
    cache.set(200, "the number 200")
    value = cache.get(200)
    assert value == "the number 200"
    assert cache.store.head.data[0] == 200
    assert cache.store.head.data[1] == "the number 200"

    # fill the cache past capacity
    for n in range(10):
        cache.set(n, n)

    # the first five should have been flushed out of the cache
    assert cache.get(0) is None
    assert cache.get(1) is None
    assert cache.get(2) is None
    assert cache.get(3) is None
    assert cache.get(4) is None
    assert cache.get(5) == 5
    assert cache.get(6) == 6
    assert cache.get(7) == 7
    assert cache.get(8) == 8
    assert cache.get(9) == 9

    # 5 is the LRU so add another item and verify it was flushed
    cache.set(47, 47)
    assert cache.get(5) is None

    # Reduce the capacity and see if we flush the extra items
    cache.capacity = 2
    cache.set(42, 'The Answer')

    assert cache.get(7) is None
    assert cache.get(8) is None
    assert cache.get(9) is None
    assert cache.get(47) == 47
    assert cache.get(42) == 'The Answer'

    # The end
    print('All cache tests pass!')
