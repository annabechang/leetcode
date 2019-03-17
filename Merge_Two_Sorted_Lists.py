"""
21. Merge Two Sorted Lists
Easy

1989

276

Favorite

Share
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        current = dummy = ListNode(0)
        while l1 and l2:
            #compare
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else: 
                current.next = l2
                l2 = l2.next
            current = current.next
        current.next = l1 or l2
        
        return dummy.next
        
"""
Success
Details 
Runtime: 48 ms, faster than 61.59% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 13.1 MB, less than 5.06% of Python3 online submissions for Merge Two Sorted Lists.
"""
