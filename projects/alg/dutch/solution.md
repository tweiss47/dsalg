# Dutch National Flag Problem

This a variation of the general dutch flag sorting where an input array is
partitioned into three groups (<, ==, and > a value in the array). In this
case the array just contains 0, 1, or 2.

The solution is `sort_012()` in `dutch.py`.

The solution keeps track of 3 indices:
1. `front` which is where to write the next 0
2. `back` which is where to write the next 2
3. `next` which is the next value to examine

The solution works in a single pass of the input list, `O(n)`. And requires
no additional space beyond the indices.

