# Finding the Square Root of an Integer

`square-root.py` contains the implementation of `sqrt()` which finds the integer
square root of a number.

The solution uses a binary search to find the square root in the interval
`[0..number]`. Because we can't test for the target value directly we have
to adjust the loop condition and the loop will exit without directly finding
the square root if the input isn't a perfect square. In which case we need
to perform a final test of the remaining boundary to values to return the
correct result.

The runtime complexity is `O(log(n))` where n is the input value. There are no
notable space requirements since the search is iterative.
