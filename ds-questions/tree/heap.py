# Implementation of a heap. The standard library heapq has the implementation
# to use, but this seemed like a good exercise. heap_introduction.ipynb has
# a lot of detail on developing a heap and served as a starting point for this
# implementation.


class Heap:
    def __init__(self, min=True):
        self.store = []
        self.next_index = 0
        self.min = min


    def __len__(self):
        """
        Return the number of elements currently stored in the Heap
        """
        assert self.next_index <= len(self.store)
        return self.next_index


    def __repr__(self):
        return str([v for v in self.store])


    def _in_heap_order(self, parent, child):
        """
        Return True of the values indexed by parent and child preserve the
        heap constraint
        """
        if self.min:
            return self.store[parent] <= self.store[child]
        else:
            return self.store[parent] >= self.store[child]


    def _next_in_heap_order(self, i, j):
        """
        Given two indexes i and j return the one that has references the
        smaller value if it is a min heap or larger value if it is a max heap
        """
        if self.min:
            return i if self.store[i] < self.store[j] else j
        else:
            return i if self.store[i] > self.store[j] else j


    def _check_is_valid(self):
        # TODO traverse the heap and return true if it valid
        pass


    def insert(self, data):
        """
        Insert data value into the Heap
        """
        # Insert the new data element at the end of the heap
        if self.next_index < len(self.store):
            self.store[self.next_index] = data
        else:
            self.store.append(data)
            self.next_index = len(self.store) - 1
        index = self.next_index
        self.next_index += 1

        assert index == self.next_index - 1
        assert self.next_index <= len(self.store)

        # Then heapify up by swapping the new node with its parent if it is
        # violating the heap ordering constraint
        while index > 0:
            parent_index = (index - 1) // 2

            # stop if we are already in order
            if self._in_heap_order(parent_index, index):
                break

            # swap and move to the parent
            temp = self.store[parent_index]
            self.store[parent_index] = self.store[index]
            self.store[index] = temp
            index = parent_index


    def remove(self):
        """
        Remove and return the element at the top of the Heap
        """
        if self.next_index == 0:
            return None

        # move the next index and swap the top element with the last
        self.next_index -= 1
        if self.next_index > 0:
            temp = self.store[0]
            self.store[0] = self.store[self.next_index]
            self.store[self.next_index] = temp

        assert self.next_index < len(self.store)

        # heapify by moving the head element down the tree until the heap
        # constraint is met
        index = 0
        while index < self.next_index:
            # find the correct child to swap
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            child = left_child_index
            if right_child_index < self.next_index:
                child = self._next_in_heap_order(left_child_index, right_child_index)

            # if we've run out of nodes or are in order stop
            if child >= self.next_index or self._in_heap_order(index, child):
                break

            # swap and move down the tree
            temp = self.store[index]
            self.store[index] = self.store[child]
            self.store[child] = temp
            index = child

        return self.store[self.next_index]


if __name__ == "__main__":
    print("Testing Heap")

    # A min heap
    h = Heap()
    assert len(h) == 0
    h.insert(47)
    assert len(h) == 1
    assert h.store[0] == 47
    h.insert(23)
    assert len(h) == 2
    assert h.store[0] == 23

    # A max heap
    h = Heap(False)
    assert len(h) == 0
    h.insert(47)
    assert len(h) == 1
    assert h.store[0] == 47
    h.insert(23)
    assert len(h) == 2
    assert h.store[0] == 47

    # Test ordering min heap

    import random
    data = [5 * i for i in range(1, 11)]
    random.shuffle(data)

    def test_ordering(data, min):
        h = Heap(min)
        for v in data:
            h.insert(v)

        result = []
        while len(h) > 0:
            result.append(h.remove())
        expected = sorted(data)
        if not min:
            expected.reverse()
        assert result == expected

    test_ordering(data, True)
    test_ordering(data, False)

    print("All tests pass!")

