class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def mirror_tree(root):
    if not root:
        return None
    root.left, root.right = root.right, root.left
    mirror_tree(root.left)
    mirror_tree(root.right)
    return root


def print_tree(root):
    res = []
    q = [root]
    while q:
        node = q.pop(0)
        if node:
            res.append(node.val)
            q.append(node.left)
            q.append(node.right)
    print(res)


t = TreeNode(1)
t.left = TreeNode(2, TreeNode(4), TreeNode(5))
t.right = TreeNode(3, TreeNode(6), TreeNode(7))
print("Исходное дерево:")
print_tree(t)
mirror_tree(t)
print("Зеркальное дерево:")
print_tree(t)
