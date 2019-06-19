# Max and Min in a Unsorted Array


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    # require at least one element rather than have a default answer like
    # (-inf, inf)
    if len(ints) == 0:
        raise ValueError("ints list is empty")
    max = min = ints[0]

    for value in ints:
        if value < min:
            min = value
        if value > max:
            max = value
    return (min, max)


if __name__ == "__main__":
    ## Example Test Case of Ten Integers
    import random

    l = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(l)

    print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

    # simple test cases
    try:
        get_min_max([])
        print("Fail, expected ValueError")
    except ValueError:
        print("Pass, ValueError raised")

    assert (47, 47) == get_min_max([47])
    assert (47, 47) == get_min_max([47, 47])
    assert (-47, 47) == get_min_max([47, 47, -47])
    assert (-1, -1) == get_min_max([-1])

    print("All tests pass")