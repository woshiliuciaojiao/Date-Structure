class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST_Builder:
    def __init__(self):
        self.root = None

    # 插入节点构建BST
    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
            return
        cur = self.root
        while True:
            if val < cur.val:
                if not cur.left:
                    cur.left = TreeNode(val)
                    break
                cur = cur.left
            else:
                if not cur.right:
                    cur.right = TreeNode(val)
                    break
                cur = cur.right

    # 和截图一致的缩进式树形打印
    def print_tree(self, node=None, prefix="", is_last=True):
        if node is None:
            node = self.root
        print(prefix + ("└── " if is_last else "├── ") + str(node.val))
        # 先左后右，和你截图顺序一致
        if node.left:
            self.print_tree(node.left, prefix + ("    " if is_last else "│   "), False)
        if node.right:
            self.print_tree(node.right, prefix + ("    " if is_last else "│   "), True)


# ========== 运行题1 ==========
if __name__ == "__main__":
    nums = [50, 30, 70, 20, 40, 60, 80]
    bst1 = BST_Builder()
    for n in nums:
        bst1.insert(n)

    print("===== 题1：构建BST =====")
    bst1.print_tree()