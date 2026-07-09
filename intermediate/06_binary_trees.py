# 06_binary_trees.py
#
# A binary search tree stores smaller values on the left
# and larger values on the right.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return TreeNode(value)

    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)

    return root


def contains(root, value):
    if root is None:
        return False

    if value == root.value:
        return True

    if value < root.value:
        return contains(root.left, value)

    return contains(root.right, value)


def inorder(root):
    if root is None:
        return []

    return inorder(root.left) + [root.value] + inorder(root.right)


root = None
for number in [50, 25, 75, 10, 30, 60, 90]:
    root = insert(root, number)

print("In-order traversal:", inorder(root))
print("Contains 30?", contains(root, 30))
print("Contains 99?", contains(root, 99))
