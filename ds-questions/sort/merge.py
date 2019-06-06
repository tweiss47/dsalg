# implement merge sort algorithm


def merge_sort(a):
    """
    Perform a merge sort of the array a
    """
    def merge(left, right):
        result = []
        i_left = i_right = 0
        while i_left < len(left) and i_right < len(right):
            if left[i_left] < right[i_right]:
                result.append(left[i_left])
                i_left += 1
            else:
                result.append(right[i_right])
                i_right += 1

        result += left[i_left:]
        result += right[i_right:]

        return result

    def merge_in_place(left, right, a):
        i = i_left = i_right = 0
        while i_left < len(left) and i_right < len(right):
            if left[i_left] < right[i_right]:
                a[i] = left[i_left]
                i_left += 1
            else:
                a[i] = right[i_right]
                i_right += 1
            i += 1

        while i_left < len(left):
            a[i] = left[i_left]
            i_left += 1
            i += 1
        while i_right < len(right):
            a[i] = right[i_right]
            i_right += 1
            i += 1
        return a

    if len(a) <= 1:
        return a

    # split and sort the input array
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])

    # merge the two halves
    # return merge(left, right)
    return merge_in_place(left, right, a)


if __name__ == "__main__":
    print(merge_sort([1]))
    print(merge_sort([1, 2]))
    print(merge_sort([2, 1]))
    print(merge_sort([1, 3, 2]))

    import random
    data = [random.randint(0, 100) for _ in range(20)]
    print(merge_sort(data))
