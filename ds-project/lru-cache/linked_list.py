'''
Implement a doubly linked list class which explicitly exposes underlying node.
This will allow for constant time removal and insertion at any point in the
list.

Not complete, only the core functionality needed for the LRU cache project is
implemented.
'''


class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return 'Node({0})'.format(self.data)


class DList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_head(self, node):
        '''Insert a DNode at the head of the list'''
        assert node

        # add node as prev of the current head
        if self.head:
            assert self.head.prev is None
            self.head.prev = node
        node.next = self.head

        # update head
        self.head = node

        # update tail if this is the only node
        if not self.tail:
            assert node.prev is None
            self.tail = self.head

    def remove_tail(self):
        '''Remove and return the node at the tail. Returns None if empty.'''
        # list is empty
        if not self.tail:
            return None

        # update the new tail (cut out the tail node)
        if self.tail.prev:
            assert self.tail.prev.next == self.tail
            self.tail.prev.next = None

        # save the old tail and reset
        old = self.tail
        self.tail = self.tail.prev

        # clean up references
        old.prev = None
        assert old.next is None

        # update the head if this was the only element
        if self.head == old:
            self.head = None

        return old


    def remove_node(self, node):
        '''Remove the node from the list. No return.'''
        assert node is not None

        # cut the node out of the list
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        # update head and tail
        if self.head == node:
            self.head = node.next
        if self.tail == node:
            self.tail = node.prev

        # clean up references
        node.next = None
        node.prev = None

    def __repr__(self):
        result = '['
        node = self.head
        while node:
            result += str(node)
            if node.next:
                result += ', '
            node = node.next
        result += ']'
        return result


if __name__ == '__main__':
    # create and print a node
    node = DNode(1)
    print(node)
    assert str(node) == 'Node(1)'

    # start with an empty list and add 3 nodes
    ll = DList()
    print(ll)
    assert str(ll) == '[]'
    ll.insert_head(node)
    assert ll.head == node
    assert ll.tail == node
    assert node.next is None
    assert node.prev is None
    print(ll)
    assert str(ll) == '[Node(1)]'

    node2 = DNode(2)
    ll.insert_head(node2)
    assert ll.head == node2
    assert ll.tail == node
    assert node.next is None
    assert node.prev is node2
    print(ll)
    assert str(ll) == '[Node(2), Node(1)]'

    node3 = DNode(3)
    ll.insert_head(node3)
    assert ll.head == node3
    assert ll.tail == node
    assert node.next is None
    assert node.prev is node2
    assert node2.next is node
    assert node2.prev is node3
    assert node3.next is node2
    assert node3.prev is None
    print(ll)
    assert str(ll) == '[Node(3), Node(2), Node(1)]'

    # remove tail nodes until the list is empty
    removed = ll.remove_tail()
    print(removed)
    assert removed == node
    assert removed.next is None
    assert removed.prev is None
    print(ll)
    assert str(ll) == '[Node(3), Node(2)]'
    assert ll.tail == node2
    assert ll.tail.next is None

    removed = ll.remove_tail()
    print(removed)
    assert removed == node2
    assert removed.next is None
    assert removed.prev is None
    print(ll)
    assert str(ll) == '[Node(3)]'
    assert ll.tail == node3
    assert ll.tail.next is None
    assert ll.head == node3
    assert ll.head.next is None

    removed = ll.remove_tail()
    print(removed)
    assert removed == node3
    assert removed.next is None
    assert removed.prev is None
    print(ll)
    assert str(ll) == '[]'
    assert ll.tail is None
    assert ll.head is None

    # call on an empty list
    removed = ll.remove_tail()
    assert removed is None

    # build up the list again and then test remove
    ll.insert_head(node)
    ll.insert_head(node2)
    ll.insert_head(node3)
    print(ll)
    assert str(ll) == '[Node(3), Node(2), Node(1)]'

    # remove the middle
    ll.remove_node(node2)
    assert node2.next is None
    assert node2.prev is None
    assert ll.head == node3
    assert node3.next == node
    assert ll.tail == node
    assert node.prev == node3
    print(ll)
    assert str(ll) == '[Node(3), Node(1)]'

    # remove the head
    ll.remove_node(node3)
    assert node3.next is None
    assert node3.prev is None
    assert ll.head == node
    assert node.next is None
    assert ll.tail == node
    assert node.prev is None
    print(ll)
    assert str(ll) == '[Node(1)]'

    # remove the tail
    ll.remove_node(node)
    assert node.next is None
    assert node.prev is None
    assert ll.head is None
    assert ll.tail is None
    print(ll)
    assert str(ll) == '[]'
