# HTTPRouter using a Trie


class RouteTrieNode:
    """Trie nodes for each path segment"""
    def __init__(self):
        self.handler = None
        self.children = {}

    def insert(self, segment, child):
        if segment not in self.children:
            self.children[segment] = child


class RouteTrie:
    """A trie for paths that resolve to handlers"""
    def __init__(self, default_handler):
        self.root = RouteTrieNode()
        self.root.handler = default_handler

    def insert(self, path, handler):
        """Add a new path and handler"""
        segments = self._get_path_segments(path)

        node = self.root
        for segment in segments:
            # insert a new node
            child = RouteTrieNode()
            node.insert(segment, child)

            # move to the new node
            node = node.children[segment]

        # add the handler to the last node
        node.handler = handler

    def find(self, path):
        """Return the handler for the given path"""
        segments = self._get_path_segments(path)
        node = self.root
        for segment in segments:
            if segment not in node.children:
                return None
            node = node.children[segment]
        return node.handler

    def _get_path_segments(self, path):
        # Helper method to clean and validate the path
        segments = path.split("/")
        # require that paths start with /
        if segments[0] != "":
            raise ValueError("path must start with a /")
        # but ignore trailing / or empty segments //
        return [s for s in segments if s != ""]



# The Router class will wrap the Trie
class Router:
    def __init__(self, default_handler, not_found_handler = None):
        self.trie = RouteTrie(default_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        self.trie.insert(path, handler)

    def lookup(self, path):
        handler = self.trie.find(path)
        return handler if handler else self.not_found_handler


if __name__ == "__main__":
    print ("Testing the router")

    # create the router and add a route
    router = Router("root handler", "not found handler")
    router.add_handler("/home/about", "about handler")

    # some lookups with the expected output
    assert "root handler" == router.lookup("/")
    assert "not found handler" == router.lookup("/home")
    assert "about handler" == router.lookup("/home/about")
    assert "about handler" == router.lookup("/home/about/")
    assert "not found handler" == router.lookup("/home/about/me")

    # add another route and verify that it works now
    router.add_handler("/home/about/me", "all about me")
    assert "all about me" == router.lookup("/home/about/me")

    # update a route
    router.add_handler("/home/about/me", "everything about me")
    assert "everything about me" == router.lookup("/home/about/me")

    # test a sloppy path with extra slashes
    assert "everything about me" == router.lookup("///home//about/////me///")

    # an empty path is okay
    assert "root handler" == router.lookup("")

    # updating the root handler is allowed
    router.add_handler("/", "new root handler")
    assert "new root handler" == router.lookup("/")

    # but don't respond to using a relative path
    try:
        handler = router.lookup("home/about")
        print("Failed, expected ValueError")
    except ValueError:
        print("Passed, expected ValueError")

    print ("All tests pass")
