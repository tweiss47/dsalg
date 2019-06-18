# Rearrange Array Elements

`rearrange.py` contains an implementation of `rearrange_digits()` which takes
an input list of digits and arranges them into two integers with a maximum sum.

The solution involves selecting the largest remaining digit and adding
alternately it to one of the output numbers. Since the input values are all in
a fixed range, rather than sorting the input list or using a heap to pick the
largest, the input is converted into a histogram. Then the counts in the histogram
can be reduced from largest to smallest for each digit written to the output.

There are two iterations of size n where n is the number of digits in the input.
So the runtime complexity is `O(n)`. Iterations of the histogram are effectively
constant since its size is fixed at 10. There is additional constant space
required to store the histogram.
