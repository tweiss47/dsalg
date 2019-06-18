# Rearrange Array Elements

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is
    maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # Need to extract the digits from input_list largest to smallest but since
    # they all fit in the range [0..9] they don't need to be sorted.

    # Make a histogram of number of occurences of each digit
    digits = [0 for _ in range(10)]
    for value in input_list:
        if value < 0 or value > 9:
            raise ValueError("input_list must only contain value between 0 an 9")
        digits[value] += 1

    result = [0, 0]
    index = 9
    count = len(input_list)
    result_index = 0
    while count > 0:
        # move index back until there is a non zero value
        while digits[index] == 0:
            index -= 1

        # add the digit to one of the output numbers
        result[result_index] *= 10
        result[result_index] += index

        # update counters
        digits[index] -= 1
        result_index = 1 if result_index == 0 else 0
        count -= 1

    return result


if __name__ == "__main__":
    # run tests from problem description
    def test_function(test_case):
        output = rearrange_digits(test_case[0])
        solution = test_case[1]
        if sum(output) == sum(solution):
            print("Pass")
        else:
            print("Fail", solution)

    test_function([[1, 2, 3, 4, 5], [542, 31]])
    test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

    # test some corner cases
    assert rearrange_digits([]) == [0, 0]
    assert rearrange_digits([1]) == [1, 0]
    assert rearrange_digits([1, 1]) == [1, 1]
    assert rearrange_digits([1, 1, 1]) == [11, 1]

    # invlid input
    try:
        rearrange_digits([1, 2, 3, 47, 9])
        print("Fail: expected ValueError")
    except ValueError:
        print("Pass")
