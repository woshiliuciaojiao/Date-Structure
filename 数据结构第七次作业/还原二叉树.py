from collections import deque


# 1. 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 2. 从层序遍历数组构建二叉树（None 表示空节点）
def build_tree(arr):
    if not arr:
        return None

    # 根节点
    root = TreeNode(arr[0])
    queue = deque([root])
    index = 1

    while queue and index < len(arr):
        current_node = queue.popleft()

        # 左孩子
        if arr[index] is not None:
            current_node.left = TreeNode(arr[index])
            queue.append(current_node.left)
        index += 1

        # 右孩子
        if index < len(arr) and arr[index] is not None:
            current_node.right = TreeNode(arr[index])
            queue.append(current_node.right)
        index += 1

    return root


# 3. 中序遍历（验证二叉搜索树性质）
def inorder_traversal(root, result=None):
    if result is None:
        result = []
    if root:
        inorder_traversal(root.left, result)
        result.append(root.val)
        inorder_traversal(root.right, result)
    return result


# 4. 层序遍历（验证构建是否正确）
def level_order_traversal(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # 去掉末尾多余的 None（可选）
    while result and result[-1] is None:
        result.pop()
    return result


# 5. 打印树的文本结构（直观查看形态）
def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.val))
        print_tree(root.left, level + 1, "L--- ")
        print_tree(root.right, level + 1, "R--- ")


# ---------------- 测试代码 ----------------
if __name__ == "__main__":
    # 题目给定的数组
    arr = [10, 5, 15, 3, 7, None, 20]

    # 构建二叉树
    root = build_tree(arr)

    # 验证层序遍历结果
    print("层序遍历结果：", level_order_traversal(root))
    # 验证中序遍历结果（二叉搜索树应是有序的）
    print("中序遍历结果：", inorder_traversal(root))
    print("\n树的文本结构：")
    print_tree(root)