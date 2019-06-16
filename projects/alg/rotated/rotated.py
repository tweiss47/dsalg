# Search in a Rotated Sorted Array

def find_partition(a):
    """
    Given a rotated array a, find the largest value and index.
    """
    # start out with the first value as the potential largest
    target = a[0]
    # do a modified binary search to find the potential largest
    low = 0
    high = len(a) - 1
    # search until the interval can't be reduced
    while high - low > 1:
        mid = (high + low) // 2
        if a[mid] >= target:
            # if we find a larger value move low up and reset the target
            target = a[mid]
            low = mid
        else:
            high = mid - 1
    return (low, a[low]) if a[high] < target else (high, a[high])


def binary_search(a, low, high, target):
    """
    Do a binary search on the interval in a defined by a[low:high] for target
    """
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == target:
            return mid
        elif a[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if len(input_list) == 0:
        return -1

    # find the partition point in the array (the largest or smallest element)
    index, value = find_partition(input_list)

    # determine the half to search in
    low = 0
    high = len(input_list) - 1

    if input_list[0] <= number <= value:
        high = index
    else:
        low = index + 1

    # do a binary search in that half
    return binary_search(input_list, low, high, number)


if __name__ == "__main__":
    # test out find_partition
    assert 1, 0 == find_partition([1])
    assert 2, 1 == find_partition([1, 2])
    assert 2, 0 == find_partition([2, 1])
    assert 3, 2 == find_partition([1, 2, 3])
    assert 3, 0 == find_partition([3, 1, 2])
    assert 3, 1 == find_partition([2, 3, 1])
    assert 9, 9 == find_partition([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert 9, 1 == find_partition([8, 9, 0, 1, 2, 3, 4, 5, 6, 7])
    assert 9, 7 == find_partition([2, 3, 4, 5, 6, 7, 8, 9, 0, 1])

    # run the tests from the problem description
    def linear_search(input_list, number):
        for index, element in enumerate(input_list):
            if element == number:
                return index
        return -1

    def test_function(test_case):
        input_list = test_case[0]
        number = test_case[1]
        if linear_search(input_list, number) == rotated_array_search(input_list, number):
            print("Pass")
        else:
            print("Fail")

    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 8])
    test_function([[6, 7, 8, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 10])

    # test out corner cases
    assert -1 == rotated_array_search([], 47)
    assert -1 == rotated_array_search([0], 47)
    assert 0 == rotated_array_search([47], 47)
