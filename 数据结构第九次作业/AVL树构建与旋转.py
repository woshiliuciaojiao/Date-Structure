class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def get_height(node):
    return node.height if node else 0

def update_height(node):
    if node:
        node.height = 1 + max(get_height(node.left), get_height(node.right))

def balance_factor(node):
    return get_height(node.left) - get_height(node.right) if node else 0

def rotate_right(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    update_height(y)
    update_height(x)
    return x

def rotate_left(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    update_height(x)
    update_height(y)
    return y

def print_tree(root, prefix="", is_left=True):
    if not root:
        return
    print(prefix + ("├── " if is_left else "└── ") +
          f"{root.key} (bf={balance_factor(root)})")
    if root.left or root.right:
        if root.left:
            print_tree(root.left, prefix + ("│   " if is_left else "    "), True)
        else:
            print(prefix + ("│   " if is_left else "    ") + "├── None")
        if root.right:
            print_tree(root.right, prefix + ("│   " if is_left else "    "), False)
        else:
            print(prefix + ("│   " if is_left else "    ") + "└── None")

def insert(root, key, step_info=None):
    if not root:
        return AVLNode(key)

    if key < root.key:
        root.left = insert(root.left, key, step_info)
    elif key > root.key:
        root.right = insert(root.right, key, step_info)
    else:
        return root

    update_height(root)
    bf = balance_factor(root)

    # LL
    if bf > 1 and balance_factor(root.left) >= 0:
        if step_info:
            step_info['unbalance'] = 'LL'
            step_info['pivot'] = root.key
        return rotate_right(root)

    # LR: 先左旋左孩子，再右旋当前节点
    if bf > 1 and balance_factor(root.left) < 0:
        if step_info:
            step_info['unbalance'] = 'LR'
            step_info['pivot'] = root.key
        print("  → LR失衡：先对左孩子左旋")
        root.left = rotate_left(root.left)
        print_tree(root, "    ")
        print("  → 再对当前节点右旋")
        return rotate_right(root)

    # RR
    if bf < -1 and balance_factor(root.right) <= 0:
        if step_info:
            step_info['unbalance'] = 'RR'
            step_info['pivot'] = root.key
        return rotate_left(root)

    # RL: 先右旋右孩子，再左旋当前节点
    if bf < -1 and balance_factor(root.right) > 0:
        if step_info:
            step_info['unbalance'] = 'RL'
            step_info['pivot'] = root.key
        print("  → RL失衡：先对右孩子右旋")
        root.right = rotate_right(root.right)
        print_tree(root, "    ")
        print("  → 再对当前节点左旋")
        return rotate_left(root)

    return root

def inorder_traversal(root, result):
    if root:
        inorder_traversal(root.left, result)
        result.append(root.key)
        inorder_traversal(root.right, result)

if __name__ == "__main__":
    sequence = [30, 20, 10, 25, 40, 35, 50]
    root = None

    for val in sequence:
        step_info = {'unbalance': None, 'pivot': None}
        print(f"\n========== 插入 {val} ==========")
        root = insert(root, val, step_info)
        print("最终树形：")
        print_tree(root)
        if step_info['unbalance']:
            print(f"⚠️ 失衡类型: {step_info['unbalance']}，旋转轴节点: {step_info['pivot']}")
        else:
            print("✅ 树保持平衡")

    inorder_result = []
    inorder_traversal(root, inorder_result)
    print("\n========== 最终树的中序遍历 ==========")
    print(inorder_result)

    # ---------- 验证 BST 性质 ----------
    is_bst = all(inorder_result[i] < inorder_result[i+1] for i in range(len(inorder_result)-1))
    if is_bst:
        print("✅ BST 性质验证通过：中序遍历结果严格升序")
    else:
        print("❌ BST 性质被破坏：中序遍历结果不是严格升序")