# Finding the Square Root of an Integer

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    # make sure that number is a valid input
    number = int(number)
    if number < 0:
        raise ValueError("number must be >= 0")

    # binary search for the square root between 0 and number
    high = number
    low = 0
    # search until you there is no integer between high and low
    while high - low > 1:
        mid = (high + low) // 2
        s = mid * mid
        if s == number:
            return mid
        elif s > number:
            high = mid - 1
        else:
            # low might be the square root
            low = mid
    # if the square root wasn't found in the loop it is one of the two values
    # not tested
    return low if high * high > number else high


if __name__ == "__main__":
    # check 0
    print ("Pass" if  (0 == sqrt(0)) else "Fail")

    # check floor behavior
    print ("Pass" if  (1 == sqrt(1)) else "Fail")
    print ("Pass" if  (1 == sqrt(2)) else "Fail")
    print ("Pass" if  (1 == sqrt(3)) else "Fail")

    # test some squares
    print ("Pass" if  (2 == sqrt(4)) else "Fail")
    print ("Pass" if  (3 == sqrt(9)) else "Fail")
    print ("Pass" if  (4 == sqrt(16)) else "Fail")
    print ("Pass" if  (5 == sqrt(25)) else "Fail")

    # test floor behavior for a larger value
    print ("Pass" if  (9 == sqrt(99)) else "Fail")
    print ("Pass" if  (10 == sqrt(100)) else "Fail")
    print ("Pass" if  (10 == sqrt(101)) else "Fail")

    # test unexpected input
    try:
        sqrt(-1)
    except ValueError:
        print("Pass")

    print ("Pass" if  (3 == sqrt(9.3)) else "Fail")

    try:
        sqrt("boo")
    except ValueError:
        print("Pass")

