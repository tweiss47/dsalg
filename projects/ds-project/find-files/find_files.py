# Search a file path for files matching a pattern


import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    # The file listing to return
    listing = list()

    # If the imput path is invalid, just return and empty list
    if not os.path.exists(path):
        return listing

    # Clean the path to avoid funky mixed delimiter
    path = os.path.normpath(path)

    # Recursively traverse the directory and all subdirectories
    def traverse(dir, pattern):
        children = os.listdir(dir)
        for file in children:
            # Concatinate the subpath to the current directory
            file = os.path.join(dir, file)
            if os.path.isfile(file):
                # Save the file if it matches the pattern
                if file.endswith(pattern):
                    listing.append(file)
            else:
                # traverse the child directory
                traverse(file, pattern)

    # Invoke the traversal and return listing
    traverse(path, suffix)
    return listing


def test_find(suffix, path, expect):
    '''
    Test find_files

        expect (list): contains a list of just the file names expected, to
        allow for testing on a different os.
    '''
    result = find_files(suffix, path)
    assert len(result) == len(expect)
    for file_name in result:
        head, tail = os.path.split(file_name)
        assert tail in expect


if __name__ == '__main__':
    print('Testing find_files()')

    # Tests assume that the script is being run from its current location in
    # the repo!

    # look for paths that exist in the test directory
    test_find('.c', './testdir', ['t1.c', 'a.c', 'b.c', 'a.c'])
    test_find('.h', './testdir', ['t1.h', 'a.h', 'b.h', 'a.h'])
    test_find('.gitkeep', './testdir', ['.gitkeep', '.gitkeep'])

    # The test function above is only validating that the file name part is
    # found, to avoid os dependencies. From this you can see that the full
    # path is returned
    listing = find_files(".c", "./testdir")
    print(listing)

    # look for an invalid suffix
    test_find('.bogus', './testdir', [])

    # look for suffixes that are only on directories
    test_find('subdir1', './testdir', [])
    test_find('1', './testdir', [])

    # This should find something - at least this script itself
    listing = find_files('.py', '..')
    # print(listing)
    assert len(listing) > 0

    # This is specific to my system, so it is commented out, but check that
    # using a full path works as expected
    # listing = find_files('.java', 'C:\\Users\\tweiss\\Source\Repos')
    # print(listing)

    print('All tests pass!')