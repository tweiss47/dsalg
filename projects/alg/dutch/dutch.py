# Dutch National Flag Problem


def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a
    single traversal.

    Args:
       input_list(list): List to be sorted
    """
    front = next = 0
    back = len(input_list) - 1
    while next <= back:
        value = input_list[next]
        if value == 0:
            # swap next to the front
            input_list[front], input_list[next] = input_list[next], input_list[front]
            front += 1
            next += 1
        elif value == 1:
            # just move next
            next += 1
        else:
            # swap next to the back and keep next in place
            input_list[back], input_list[next] = input_list[next], input_list[back]
            back -= 1
    return input_list


if __name__ == "__main__":
    # run tests from problem description

    # the way this test function is written it seems like it assumes we are making a
    # copy of the array
    def test_function(test_case):
        sorted_array = sort_012(test_case)
        if sorted_array == sorted(test_case):
            print("Pass")
        else:
            print("Fail", sorted_array)

    test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
    test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
    test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])


    # test the basic cases
    assert sort_012([]) == []
    assert sort_012([0]) == [0]
    assert sort_012([1]) == [1]
    assert sort_012([2]) == [2]
    assert sort_012([0, 1]) == [0, 1]
    assert sort_012([1, 0]) == [0, 1]
    assert sort_012([1, 2]) == [1, 2]
    assert sort_012([2, 1]) == [1, 2]
    assert sort_012([0, 1, 2]) == [0, 1, 2]
    assert sort_012([0, 2, 1]) == [0, 1, 2]
    assert sort_012([1, 0, 2]) == [0, 1, 2]
    assert sort_012([1, 2, 0]) == [0, 1, 2]
    assert sort_012([2, 1, 0]) == [0, 1, 2]
    assert sort_012([2, 0, 1]) == [0, 1, 2]

