class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST_Deleter:
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

    # 缩进式树形打印（和截图一致）
    def print_tree(self, node=None, prefix="", is_last=True):
        if node is None:
            node = self.root
        print(prefix + ("└── " if is_last else "├── ") + str(node.val))
        if node.left:
            self.print_tree(node.left, prefix + ("    " if is_last else "│   "), False)
        if node.right:
            self.print_tree(node.right, prefix + ("    " if is_last else "│   "), True)

    # 查找中序前驱（左子树最大值）
    def get_predecessor(self, node):
        cur = node.left
        while cur.right:
            cur = cur.right
        return cur

    # 中序前驱删除策略
    def delete_by_pre(self, val):
        def _del(node, val):
            if not node:
                return None
            if val < node.val:
                node.left = _del(node.left, val)
            elif val > node.val:
                node.right = _del(node.right, val)
            else:
                # 叶子/单侧子树情况
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                # 左右都有子树，用前驱替换
                pre = self.get_predecessor(node)
                node.val = pre.val
                node.left = _del(node.left, pre.val)
            return node
        self.root = _del(self.root, val)

    # 查找中序后继（右子树最小值）
    def get_successor(self, node):
        cur = node.right
        while cur.left:
            cur = cur.left
        return cur

    # 中序后继删除策略
    def delete_by_suc(self, val):
        def _del(node, val):
            if not node:
                return None
            if val < node.val:
                node.left = _del(node.left, val)
            elif val > node.val:
                node.right = _del(node.right, val)
            else:
                # 叶子/单侧子树情况
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                # 左右都有子树，用后继替换
                suc = self.get_successor(node)
                node.val = suc.val
                node.right = _del(node.right, suc.val)
            return node
        self.root = _del(self.root, val)

# ========== 运行题2 ==========
if __name__ == "__main__":
    nums = [50, 30, 70, 20, 40, 60, 80]

    # --- 方法1：中序前驱删除 ---
    print("===== 题2-1：中序前驱删除根节点50 =====")
    bst_pre = BST_Deleter()
    for n in nums:
        bst_pre.insert(n)
    bst_pre.delete_by_pre(50)
    bst_pre.print_tree()
    print("\n" + "-"*30 + "\n")

    # --- 方法2：中序后继删除 ---
    print("===== 题2-2：中序后继删除根节点50 =====")
    bst_suc = BST_Deleter()
    for n in nums:
        bst_suc.insert(n)
    bst_suc.delete_by_suc(50)
    bst_suc.print_tree()
    #注意：两种方法能混用吗？
    # 不可以混用，原因：
    #单次删除只能固定选一种策略：要么用前驱替换，要么用后继替换，不能一部分节点用前驱、一部分用后继处理同一轮删除；
    #混用会破坏 BST 的有序性，导致子树大小关系混乱，后续查找、遍历都会出错；
    #多次删除时也不建议频繁来回切换策略，虽然单次删除选其一都合法，但混用会让树结构波动更大，容易加剧树的不平衡，增加后续操作时间开销，工程上会统一固定一种策略维护一致性。
