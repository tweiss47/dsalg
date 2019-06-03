# Union and Intersection of Linked Lists

The goals for the project excercises suggest that the solutions should be and
*efficient* for each of the problems. This problem is interesting in that it
is implementing `set` operations on a linked list which is at the opposite
end of the collections spectrum in terms of performance characteristics.
Lists don't allow random access so they are can't be efficiently searched.
While sets are intended to provide constant time for find operations.

So directly implementing intersection and union on the lists will require
O(n) traversals to find elements. The simple algorithm for intersection would
be to iterate the elements in set a and test for membership in set b. Putting
the result in the output set if the test is positive. This would be O(nm)
where n is the size of a and m the size of b. Union is similar: iterate a
and test if the result is in the output if not add it; then do the same for b.
Again you get a result that is O(n^2).

An efficient implemtnation could to use a set to store the data where the
membership test is occuring. Using the intersection and union operations of
the set directly though doesn't seem like the best option since all the data
need to be moved in and out of sets to return the linked list structure.
