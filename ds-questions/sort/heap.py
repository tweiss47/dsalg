# heap sort implementation


def heap_sort(a):
    def swap(a, i, j):
        # pythonic swap
        a[i], a[j] = a[j], a[i]

    # heapify the list a by bubbling up values from the end of the list
    for c in range(len(a) - 1, 0, -1):
        while c > 0:
            p = (c - 1) // 2
            if a[p] > a[c]:
                break
            swap(a, c, p)
            c = p

    # move each top element to the end of the list and push the top down to
    # keep the heap ordering
    last = len(a) - 1
    while last > 0:
        # move the top (largest) element into the last position
        swap(a, last, 0)
        last -= 1
        # push down the top element into the right spot in the head
        p = 0
        while p < last:
            # find the largest child
            c = lc = p * 2 + 1
            rc = p * 2 + 2
            if lc > last:
                break
            if rc <= last and a[rc] > a[lc]:
                c = rc

            # move the largest child up if it is larger than a[p]
            if a[c] <= a[p]:
                break
            swap(a, c, p)
            p = c


if __name__ == "__main__":
    a = [8, 3, 1, 7, 0, 10, 2]
    heap_sort(a)
    print(a)

    a = []
    heap_sort(a)
    print(a)

    a = [47]
    heap_sort(a)
    print(a)

    a = [1, 2]
    heap_sort(a)
    print(a)

    a = [2, 1]
    heap_sort(a)
    print(a)
