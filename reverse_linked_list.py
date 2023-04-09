class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse_linked_list(head):
    prev = None
    curr = head
    # the below line can be implemented or not
    # next = None

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev


# create linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

# reverse linked list
new_head = reverse_linked_list(head)

# print reversed linked list
while new_head is not None:
    print(new_head.value)
    new_head = new_head.next
