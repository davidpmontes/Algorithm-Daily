# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        curr = head
        remainder = 0
        
        while l1 or l2:
            val1 = 0
            val2 = 0
            if l1:
                val1 = l1.val
            if l2:
                val2 = l2.val
            total = val1 + val2 + remainder
            if total >= 10:
                total -= 10
                remainder = 1
            else:
                remainder = 0
            curr.next = ListNode(total)
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        if l1 or l2:
            if l1: curr = ListNode(l1.val + remainder)
            if l2: curr = ListNode(l2.val + remainder)
        
            if curr.val >= 10:
                curr.val -= 10
                curr.next = ListNode(1)
        elif remainder:
            curr.next = ListNode(1)
            
        return head.next
