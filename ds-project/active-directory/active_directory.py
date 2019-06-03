# Provide efficient group lookup for a user/group hierarchy

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = set()

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.add(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    # A group forms the root of a tree of contained groups
    # Assume that there are no cycles - a group cannot be contained in itself

    # If the user is found in our list of users, return true
    if user in group.get_users():
        return True

    # Recursively check in each of our child groups
    for child_group in group.get_groups():
        if is_user_in_group(user, child_group):
            return True

    # User not found in this group or any child
    return False


if __name__ == "__main__":
    print("Testing Active Directory")

    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    # check for users directly in the group
    assert is_user_in_group(sub_child_user, sub_child)
    child.add_user("in_child")
    assert is_user_in_group("in_child", child)
    parent.add_user("in_parent")
    assert is_user_in_group("in_parent", parent)

    # check for user contained in a child
    assert is_user_in_group(sub_child_user, child)
    assert is_user_in_group("in_child", parent)

    # check for user contained in a grand child
    assert is_user_in_group(sub_child_user, parent)

    # check for user that does not exist
    assert not is_user_in_group("not_a_user", parent)

    # check when group has multiple sub groups
    second_child = Group("second_child_group")
    parent.add_group(second_child)
    assert not is_user_in_group("second_child_user", parent)
    second_child.add_user("second_child_user")
    assert is_user_in_group("second_child_user", parent)

    print("All tests pass!")

