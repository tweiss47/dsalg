# implement set union and intersection operations on a linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"Node({self.data})"


class LinkedList:
    """
    A list of nodes with a head and tail for efficient insertions at either
    end. And an internal count of elements. Assumes that that nodes are added
    and removed only through methods and the head is not reset.
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def __len__(self):
        return self.count

    def __str__(self):
        parts = ["["]
        node = self.head
        while node:
            parts.append(str(node))
            if node != self.tail:
                parts.append(",")
            node = node.next
        parts.append("]")
        return "".join(parts)

    def insert_head(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        if not self.tail:
            self.tail = node
        self.count += 1

    def insert_tail(self, value):
        node = Node(value)
        if not self.tail:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.count += 1

    def append(self, value):
        return self.insert_tail(value)

    # other methods not needed for this project


# helper to insert the values of a list into the values set
def insert_values(ll, values):
    node = ll.head
    while node:
        values.add(node.data)
        node = node.next


def union(lhs, rhs):
    """
    Return a LinkedList that is the union of the two LinkedList parameters
    """
    # iterate each list and insert the value into a set
    values = set()

    insert_values(lhs, values)
    insert_values(rhs, values)

    # convert the set to a list to return
    result = LinkedList()
    for v in values:
        result.insert_tail(v)
    return result


def intersection(lhs, rhs):
    """
    Return a LinkedList that is the intersection of the two LinkedList
    parameters
    """
    # add the elements of lhs to a set
    values = set()
    insert_values(lhs, values)

    result = LinkedList()

    # for each element of rhs check if it is in the set
    # add to the result if it is
    duplicates = set()
    node = rhs.head
    while node:
        if node.data in values and node.data not in duplicates:
            result.insert_head(node.data)
            duplicates.add(node.data)
        node = node.next

    return result


if __name__ == "__main__":
    print("Test the LinkedList")

    # Test the node
    node = Node(47)
    assert str(node) == "Node(47)"
    assert node.data == 47
    assert node.next is None

    # Test an empty list
    ll = LinkedList()
    assert str(ll) == "[]"
    assert ll.head is None
    assert ll.tail is None
    assert len(ll) == 0

    # Test a single element list
    ll = LinkedList()
    ll.insert_head(47)
    assert str(ll) == "[Node(47)]"
    assert ll.head == ll.tail
    assert len(ll) == 1

    ll = LinkedList()
    ll.insert_tail(47)
    assert str(ll) == "[Node(47)]"
    assert ll.head == ll.tail
    assert len(ll) == 1

    # Test a two element list, adding at the front
    ll = LinkedList()
    ll.insert_head(1)
    node = ll.head
    ll.insert_head(2)
    assert str(ll) == "[Node(2),Node(1)]"
    assert ll.tail == node
    assert ll.tail.data == 1
    assert ll.head.data == 2
    assert len(ll) == 2

    # Test a two element list, adding at the end
    ll = LinkedList()
    ll.insert_tail(1)
    node = ll.head
    ll.insert_tail(2)
    assert str(ll) == "[Node(1),Node(2)]"
    assert ll.head == node
    assert ll.tail.data == 2
    assert ll.head.data == 1
    assert len(ll) == 2

    print("LinkedList tests pass!")

    print("Testing union and intersection")

    def test_set_operations(lhs, rhs):
        """
        Use the two python lists lhs and rhs to test the intersection and
        union functions
        """
        # build a linked list from the input
        def linked_list_from_list(a):
            result = LinkedList()
            for value in a:
                result.append(value)
            return result

        lhs_list = linked_list_from_list(lhs)
        rhs_list = linked_list_from_list(rhs)

        union_list = union(lhs_list, rhs_list)
        inter_list = intersection(lhs_list, rhs_list)

        union_set = set(lhs).union(set(rhs))
        inter_set = set(lhs).intersection(set(rhs))

        print("union", union_list, union_set)
        print("inter", inter_list, inter_set)

        def check_set_result(list_result, set_result):
            # They should be the same size and all the elements in the list
            # should be in the set
            if len(list_result) != len(set_result):
                return False
            node = list_result.head
            while node:
                if node.data not in set_result:
                    return False
                node = node.next
            return True

        assert check_set_result(union_list, union_set)
        assert check_set_result(inter_list, inter_set)

    # Sample test case 1 from problem description
    test_set_operations(
        [3,2,4,35,6,65,6,4,3,21],
        [6,32,4,9,6,1,11,21,1]
    )

    # Sample test case 2 from problem description
    test_set_operations(
        [3,2,4,35,6,65,6,4,3,23],
        [1,7,8,9,11,21,1]
    )

    test_set_operations([], [])
    test_set_operations([1], [2])
    test_set_operations([2], [2])
    test_set_operations([2, 2], [2, 2])
    test_set_operations([2, 3], [3, 2])

    print("Union and intersection tests pass!")

