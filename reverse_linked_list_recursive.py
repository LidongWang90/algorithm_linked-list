# 没搞明白。需要继续！
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse_linked_list(head):
    if head is None or head.next is None:
        return head

    new_head = reverse_linked_list(head.next)
    head.next.next = head
    head.next = None
    return new_head


# create linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

# reverse linked list recursively
new_head = reverse_linked_list(head)

# print reversed linked list
while new_head is not None:
    print(new_head.value)
    new_head = new_head.next
