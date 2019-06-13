# implementation of quick sort


def pivot_first(a, start, end):
    # pivot around the first element
    while start < end:
        if a[start + 1] < a[start]:
            temp = a[start]
            a[start] = a[start + 1]
            a[start + 1] = temp
            start += 1
        else:
            temp = a[start + 1]
            a[start + 1] = a[end]
            a[end] = temp
            end -= 1
    return start


def pivot_last(a, start, end):
    # Using the last element as the pivot means only 1.5 writes to the list per
    # iteration. 2 are used when the first element is used as a pivot
    pivot_value = a[end]
    while start < end:
        value = a[start]
        if value < pivot_value:
            start += 1
            continue

        a[end] = value
        end -= 1
        a[start] = a[end]
        a[end] = pivot_value
    return end



def quick_sort(a):
    def quick(a, start, end):
        if end <= start:
            return

        # part = pivot_first(a, start, end)
        part = pivot_last(a, start, end)

        # recursive pivot for each remaining half
        quick(a, start, part - 1)
        quick(a, part + 1, end)

    quick(a, 0, len(a) - 1)


if __name__ == "__main__":
    a = [8, 3, 1, 7, 0, 10, 2]
    quick_sort(a)
    print(a)

    a = []
    quick_sort(a)
    print(a)

    a = [47]
    quick_sort(a)
    print(a)

    a = [1, 2]
    quick_sort(a)
    print(a)

    a = [2, 1]
    quick_sort(a)
    print(a)
