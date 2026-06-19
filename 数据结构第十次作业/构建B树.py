class BTreeNode:
    def __init__(self, leaf=True):
        self.keys = []
        self.children = []
        self.leaf = leaf

class BTree:
    def __init__(self, m):
        self.m = m
        self.max_cnt = m - 1   # 3阶B树：单个节点最多存放 2 个关键字
        self.root = BTreeNode()

    # 分裂：节点凑满3个关键字后排序，取下标1的关键字上移分裂
    def split(self, parent, idx):
        node = parent.children[idx]
        # 先排序，保证关键字有序
        node.keys.sort()
        mid = 1
        up_key = node.keys[mid]

        # 拆分关键字
        left_keys = node.keys[:mid]
        right_keys = node.keys[mid+1:]

        node.keys = left_keys
        new_node = BTreeNode(leaf=node.leaf)
        new_node.keys = right_keys

        # 拆分子节点
        if not node.leaf:
            new_node.children = node.children[mid+1:]
            node.children = node.children[:mid+1]

        # 中间关键字上升到父节点
        parent.keys.insert(idx, up_key)
        parent.children.insert(idx+1, new_node)

    def insert_val(self, node, val):
        # 叶子节点：直接添加并排序，满3个关键字再触发分裂
        if node.leaf:
            node.keys.append(val)
            node.keys.sort()
            return

        # 非叶子节点：寻找对应子节点
        i = len(node.keys) - 1
        while i >= 0 and val < node.keys[i]:
            i -= 1
        i += 1
        child = node.children[i]

        # 递归向子节点插入数据
        self.insert_val(child, val)

        # 子节点达到3个关键字，执行分裂
        if len(child.keys) > self.max_cnt:
            self.split(node, i)

    def insert(self, val):
        self.insert_val(self.root, val)
        # 根节点溢出，新建根并分裂
        if len(self.root.keys) > self.max_cnt:
            new_root = BTreeNode(leaf=False)
            new_root.children.append(self.root)
            self.split(new_root, 0)
            self.root = new_root

    # 树形打印
    def print_tree(self, node, depth=0):
        print("    " * depth + str(node.keys))
        if not node.leaf:
            for c in node.children:
                self.print_tree(c, depth + 1)

    # 中序遍历
    def in_order(self, node, res):
        for i in range(len(node.keys)):
            if not node.leaf:
                self.in_order(node.children[i], res)
            res.append(node.keys[i])
        if not node.leaf:
            self.in_order(node.children[-1], res)

    # 详细B树性质校验
    def check(self):
        all_ok = True
        m = self.m
        max_k = self.max_cnt
        min_k = (m // 2) - 1
        detail = []

        # 1. 校验所有叶子节点处于同一层
        leaf_depth = None
        def get_d(n, d):
            nonlocal leaf_depth
            if n.leaf:
                if leaf_depth is None:
                    leaf_depth = d
                return
            for c in n.children:
                get_d(c, d+1)
        get_d(self.root, 0)

        leaf_same = True
        def chk_d(n, d):
            nonlocal leaf_same
            if n.leaf:
                if d != leaf_depth:
                    leaf_same = False
                return
            for c in n.children:
                chk_d(c, d+1)
        chk_d(self.root, 0)
        detail.append(f"1. 所有叶子节点层数一致：{'✅ 符合规则' if leaf_same else '❌ 不符合规则'}")
        if not leaf_same:
            all_ok = False

        # 2. 校验关键字数量范围
        key_num_ok = True
        def chk_key(n, is_root=False):
            nonlocal key_num_ok
            cnt = len(n.keys)
            if is_root:
                if not (1 <= cnt <= max_k):
                    key_num_ok = False
            else:
                if not (min_k <= cnt <= max_k):
                    key_num_ok = False
            if not n.leaf:
                for c in n.children:
                    chk_key(c)
        chk_key(self.root, True)
        detail.append(f"2. 关键字数量合规：根节点[1,{max_k}]，普通节点[{min_k},{max_k}]  {'✅ 符合规则' if key_num_ok else '❌ 不符合规则'}")
        if not key_num_ok:
            all_ok = False

        # 3. 校验内部节点子节点数量规则
        child_cnt_ok = True
        def chk_child(n):
            nonlocal child_cnt_ok
            if not n.leaf:
                if len(n.children) != len(n.keys) + 1:
                    child_cnt_ok = False
                for c in n.children:
                    chk_child(c)
        chk_child(self.root)
        detail.append(f"3. 内部节点：子节点数 = 关键字数 + 1  {'✅ 符合规则' if child_cnt_ok else '❌ 不符合规则'}")
        if not child_cnt_ok:
            all_ok = False

        # 4. 校验关键字整体有序
        seq = []
        self.in_order(self.root, seq)
        order_ok = (seq == sorted(seq))
        detail.append(f"4. 关键字整体升序排列：{'✅ 符合规则' if order_ok else '❌ 不符合规则'}")
        detail.append(f"   中序遍历结果：{seq}")
        if not order_ok:
            all_ok = False

        detail.append(f"\n综合判定：当前3阶B树  {'✅ 完全合法' if all_ok else '❌ 存在错误'}")
        return detail

if __name__ == "__main__":
    t = BTree(m=3)
    data = [10, 20, 5, 6, 12, 30, 25]
    for num in data:
        print(f"----- 插入元素 {num} -----")
        # 先插入，再打印，同步显示当前最新结构
        t.insert(num)
        t.print_tree(t.root)

    print("\n========== 最终 B 树结构 ==========")
    t.print_tree(t.root)

    print("\n========== B树性质详细校验 ==========")
    check_info = t.check()
    for line in check_info:
        print(line)