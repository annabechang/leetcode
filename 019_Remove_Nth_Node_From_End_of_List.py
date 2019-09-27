"""
19. Remove Nth Node From End of List
Medium

2168

160

Favorite

Share
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        #define dummy node
        dummy = ListNode(0)
        dummy.next = head
         
        slow = fast = dummy
        
        for i in range(n):
            fast = fast.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        


"""
Success
Details 
Runtime: 44 ms, faster than 23.31% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 13.7 MB, less than 6.06% of Python3 online submissions for Remove Nth Node From End of List.

"""
