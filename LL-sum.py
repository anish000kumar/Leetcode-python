'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807. 
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = current = ListNode(None)
        quotient = 0
        while l1 or l2 or quotient:
            (v1, l1) = (l1.val, l1.next) if l1 else (0, None)
            (v2, l2) = (l2.val, l2.next) if l2 else (0, None)
            total = quotient + v1 + v2
            (quotient, remainder) = divmod(total, 10)
            current.next = current = ListNode(remainder)
        return head.next
