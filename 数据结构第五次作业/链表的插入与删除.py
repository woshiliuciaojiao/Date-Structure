class Node:
    """节点类：存储字符串数据"""
    def __init__(self, data):
        self.data = data      # 存 "hello", "world" 等
        self.next_node = None # 指向下一个节点

class LinkedList:
    """单向链表类：支持 hello world 等字符串操作"""
    def __init__(self):
        self.first_node = None  # 链表头节点，初始为空

    def insert_at_index(self, index: int, data):
        """
        在指定索引插入节点（0-based）
        逻辑与你上课课件完全一致
        """
        if index < 0:
            return False

        new_node = Node(data)

        # 特殊情况：头插
        if index == 0:
            new_node.next_node = self.first_node
            self.first_node = new_node
            return True

        current_node = self.first_node
        current_index = 0

        # 核心：找到插入位置的前一个节点
        while current_node is not None and current_index < index - 1:
            current_node = current_node.next_node
            current_index += 1

        # 越界检查
        if current_node is None:
            return False

        # 插入：先连后面，再断前面
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node
        return True

    def delete_at_index(self, index: int):
        """删除指定索引的节点"""
        if not self.first_node or index < 0:
            return False

        # 删除头节点
        if index == 0:
            self.first_node = self.first_node.next_node
            return True

        current_node = self.first_node
        current_index = 0

        # 找到待删节点的前一个节点
        while current_node is not None and current_index < index - 1:
            current_node = current_node.next_node
            current_index += 1

        # 检查是否越界
        if current_node is None or current_node.next_node is None:
            return False

        # 删除：跳过下一个节点
        current_node.next_node = current_node.next_node.next_node
        return True

    def __str__(self):
        """
        打印格式：LinkedList([hello, world, beautiful, !])
        与你图片中的输出完全一致
        """
        elements = []
        current = self.first_node
        while current:
            elements.append(str(current.data))
            current = current.next_node
        return f"LinkedList([{', '.join(elements)}])"

# ------------------- 测试：完全按照你的图片操作 -------------------
if __name__ == "__main__":
    # 1. 初始化一个空链表
    test_list = LinkedList()

    # 2. 按图片指令插入数据
    test_list.insert_at_index(0, "world")   # 头插 world
    test_list.insert_at_index(0, "hello")   # 头插 hello
    test_list.insert_at_index(2, "!")       # 尾插 !
    test_list.insert_at_index(2, "beautiful") # 中间插 beautiful

    # 3. 打印插入结果
    print(f"插入后: {test_list}")

    # 4. 演示“删除操作”（操作4）
    # 例：删除 index=2 的节点 (即 "beautiful")
    test_list.delete_at_index(1)
    print(f"删除后: {test_list}")