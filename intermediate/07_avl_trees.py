# 07_avl_trees.py
#
# An AVL tree is a binary search tree that keeps itself balanced.
# Balance helps search, insert, and delete stay efficient.

class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


def height(node):
    if node is None:
        return 0
    return node.height


def update_height(node):
    node.height = 1 + max(height(node.left), height(node.right))


def balance_factor(node):
    if node is None:
        return 0
    return height(node.left) - height(node.right)


def rotate_right(old_root):
    new_root = old_root.left
    moved_subtree = new_root.right

    new_root.right = old_root
    old_root.left = moved_subtree

    update_height(old_root)
    update_height(new_root)
    return new_root


def rotate_left(old_root):
    new_root = old_root.right
    moved_subtree = new_root.left

    new_root.left = old_root
    old_root.right = moved_subtree

    update_height(old_root)
    update_height(new_root)
    return new_root


def insert(root, value):
    if root is None:
        return AVLNode(value)

    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    else:
        return root

    update_height(root)
    balance = balance_factor(root)

    # Left left case
    if balance > 1 and value < root.left.value:
        return rotate_right(root)

    # Right right case
    if balance < -1 and value > root.right.value:
        return rotate_left(root)

    # Left right case
    if balance > 1 and value > root.left.value:
        root.left = rotate_left(root.left)
        return rotate_right(root)

    # Right left case
    if balance < -1 and value < root.right.value:
        root.right = rotate_right(root.right)
        return rotate_left(root)

    return root


def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.value] + inorder(root.right)


root = None
for number in [30, 20, 10, 25, 40, 50, 45]:
    root = insert(root, number)

print("In-order traversal:", inorder(root))
print("Root value after balancing:", root.value)
print("Root height:", root.height)
