'''
Given the head of a singly linked list, return true if it is a 
palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true
'''
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# method 1:


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # First, tranverse the linked list and store the elements in the list
        res_list = []
        while head:
            res_list.append(head.val)
            head = head.next
        # Second, check if the list is Palindrome
        left, right = 0, len(res_list) - 1
        while left <= right:
            if res_list[left] != res_list[right]:
                return False
            left += 1
            right -= 1
        return True

# method 2:


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # First, tranverse the linked list and store the elements in the list

        curr = head
        l = []
        while curr:
            l.append(curr.val)
            curr = curr.next

        curr = head
        while curr:
            if curr.val != l.pop():
                return False
            curr = curr.next
        return True
