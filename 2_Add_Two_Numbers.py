"""
2. Add Two Numbers
Medium

4851

1228

Favorite

Share
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        carry = 0 # Decimal carry 
        dummy = ListNode(0); 
        p = dummy #since the for loop go over from 7 to 0 to 8
        #at the end we need to print from 7. thus we need a pointer dummy
        # pointing at 7 
        
        #when l1, l2 both exist and have same lenth
        while l1 and l2:
            p.next = ListNode((l1.val + l2.val + carry) %10) 
            carry = (l1.val + l2.val + carry) //10  #/10
            l1 = l1.next
            l2 = l2.next
            p = p.next
            
        #l1: 2->4->3 
        #l2: 5->6->4->1
        if l2:
            while l2:
                p.next = ListNode((l2.val + carry) % 10)
                carry = (l2.val + carry) // 10 
                l2 = l2.next
                p = p.next
        
        #l1: 2->4->3->1
        #l2: 5->6->4
        if l1:
            while l1:
                p.next = ListNode((l1.val + carry) % 10)
                carry = (l1.val + carry) // 10
                l1 = l1.next
                p = p.next
        
        #the highest has one carry 
        #l1: 2->4->3
        #l2: 5->6->8 
        #3+8 > 10
        if carry ==1:
            p.next = ListNode(1)
            
        return dummy.next
        
"""        
Success
Details 
Runtime: 96 ms, faster than 86.09% of Python3 online submissions for Add Two Numbers.
Memory Usage: 13.2 MB, less than 5.21% of Python3 online submissions for Add Two Numbers.
"""        
        
