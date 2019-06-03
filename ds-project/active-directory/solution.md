# Active Directory

The goal of this exercise is to perform a group membership check for a user
when the user may be contained in a specified group or one of its contained
groups.

The solution is implemented in the `is_user_in_group()` function which
performs a check for membership in the set of users that belong to the given
group, then recursively explores any contained groups if the user is not
found.

The sample user group code just stored the group member names in a list. The
runtime performance of this implementation would be O(n) where n is the
number of groups and group memberships contained in the hierarchy. The number
of groups in the hierarchy would have a greater impact on the performance
since we need to perform a recursive call for each group encountered on the
search.

If the users were stored in a hashed container like a `dict`, then the user
lookup could be done in constant time and the runtime would then only depend
on the number of groups encountered. I used a `set` to store the user names
since only the names are stored in this example.

There may be a small storage overhead introduced by switching from a list to
a set. Lists will allocate additional space for expansion while extra hash
buckets are required for a set. Both will be proportional to the number of
group memberships stored. At runtime, using recursion will require stack space
proportional to the depth of the group containment tree.
