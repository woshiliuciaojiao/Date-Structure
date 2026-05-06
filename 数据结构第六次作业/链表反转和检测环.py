class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse(head: ListNode) -> ListNode:
    # 定义三个指针
    prev = None    # 前一个节点
    curr = head    # 当前节点
    next_node = None  # 临时保存下一个节点

    while curr is not None:
        # 1. 先保存下一个节点
        next_node = curr.next
        # 2. 反转当前节点的 next 指针
        curr.next = prev
        # 3. prev 和 curr 都向前走一步
        prev = curr
        curr = next_node

    # prev 会停在新的头节点
    return prev
def has_cycle(head: ListNode) -> bool:
    # 边界情况：空链表或只有一个节点，不可能有环
    if head is None or head.next is None:
        return False

    slow = head  # 慢指针，一次走1步
    fast = head  # 快指针，一次走2步

    # 循环条件：fast 和 fast.next 不为空，防止越界
    while fast is not None and fast.next is not None:
        slow = slow.next        # 慢指针走1步
        fast = fast.next.next   # 快指针走2步

        if slow == fast:  # 相遇了，说明有环
            return True

    # 循环结束，快指针走到了头，说明无环
    return False
# 辅助函数：打印链表（无环时用）
def print_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)
# 测试1：反转链表
print("===== 测试链表反转 =====")
# 构建链表 1→2→3→4
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
print("原链表：")
print_list(head)
new_head = reverse(head)
print("反转后：")
print_list(new_head)
# 测试2：检测环
print("\n===== 测试检测环 =====")
# 有环链表：1→2→3→2
head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = ListNode(3)
head2.next.next.next = head2.next  # 3指向2，形成环
print("有环链表检测结果：", has_cycle(head2))  # 输出True

# 无环链表：1→2→3
head3 = ListNode(1)
head3.next = ListNode(2)
head3.next.next = ListNode(3)
print("无环链表检测结果：", has_cycle(head3))  # 输出False
