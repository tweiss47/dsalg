# Find files solution

The solution for the find in files project uses a recursive directory
traversal to get a listing of all the files below the given path. Any files
that have a suffix matching input pattern are saved to the output list.

Since this is a generalized tree traversal the rutime would be proportional
to the total number of files inspected. But since each directory in
encountered results in another recursive call and another `os.listdir()`
call, the runtime likely depends almost completely on the number of
directores encountered.

A recursive traversal will require call stack space proportional to the
degree of directory nesting from the parent path.
