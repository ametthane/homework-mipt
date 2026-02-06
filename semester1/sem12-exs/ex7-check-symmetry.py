class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def check_symmetry(root):
    if not root:
        return True

    def mirror_check(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val
                and mirror_check(left.left, right.right)
                and mirror_check(left.right, right.left))

    return mirror_check(root.left, root.right)


t1 = TreeNode(1)
t1.left = TreeNode(2, TreeNode(3), TreeNode(4))
t1.right = TreeNode(2, TreeNode(4), TreeNode(3))
print(check_symmetry(t1))  # Вывод: True
t2 = TreeNode(2)
t2.left = TreeNode(5, TreeNode(7), TreeNode(8))
t2.right = TreeNode(3, TreeNode(6), TreeNode(4))
print(check_symmetry(t2))  # Вывод: False
