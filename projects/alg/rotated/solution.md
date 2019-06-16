# Search in a Rotated Sorted Array

`rotated.py` contains the implementation of `rotated_array_search()` which
implements the search for a target value in a sorted and rotated array.

Before rotation, the array is assumed to be sorted in ascending order and
to contain unique values.

The approach to the solution is to find the pivot point around which the
array is rotated. For instance, if the array is `[4, 5, 6, 7, 0, 1, 2]`, then
the array was rotated 4 spaces to the right (or 3 left) and the indices 3, 4
represent the original last and first indices (len()-1 and 0) of the array.

The value in the rotated array make two sorted sub arrays `a[0:4]` and `a[4:0]`.
So if the pivot point can be found then we can decide which sub array the target
would be in and just do a binary search on that target.

The first part of the solution is implemented in `find_partition()` which does
a modified binary search to find the largest value in the array (one before
the pivot) and returns the value and index. Since it operates by dividing the
array in half each time it has a run time of `O(log(n))`. Determining which sub
array to search is a constant time operation. And then the binary search of the
sub array will also be `O(log(n))`.

There are no additional space requirements for this algorithm.
