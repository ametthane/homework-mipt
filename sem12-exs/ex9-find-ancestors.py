class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_ancestors(root, tv):
    def find_path(node, tg, path):
        if not node:
            return False
        path.append(node.val)
        if node.val == tg:
            return True
        if (find_path(node.left, tg, path) or
                find_path(node.right, tg, path)):
            return True
        path.pop()
        return False
    path = []
    find_path(root, tv, path)
    return path[:-1] if path else []


t = TreeNode(1)
t.left = TreeNode(2, TreeNode(4, TreeNode(7)), TreeNode(5))
t.right = TreeNode(3, None, TreeNode(6))
tgs = [7, 5, 3, 1]
for tg in tgs:
    ans = find_ancestors(t, tg)
    print(f"Предки узла {tg}: {ans}")
