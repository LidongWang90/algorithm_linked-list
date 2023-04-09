class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    # 增
    def insertNode(self, head, val):
        # dummy:
        # dummy.next 永远指向处理过后的链表的head
        # 方便处理head等于null的特殊情况
        dummy = ListNode(float('-inf'))
        dummy.next = head
        curr_node = dummy
        while curr_node.next and curr_node.next <= val:
            curr_node = curr_node.next
        new_node = ListNode(val)
        new_node.next = curr_node.next
        curr_node.next = new_node
        return dummy.next

    # 删除：
    def removeElements(self, head, val):
        dummy = ListNode(float('-inf'))
        dummy.next = head
        curr_node = dummy
        while curr_node.next:
            if curr_node.next.val == val:
                curr_node.next = curr_node.next.next
            else:
                curr_node = curr_node.next
        return dummy.next

    # 寻找中点：
    def middleNode(self, head):
        if head is None:
            return None
        fast = head
        slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # rotate
