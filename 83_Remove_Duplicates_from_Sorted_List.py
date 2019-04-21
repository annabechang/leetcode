"""
83. Remove Duplicates from Sorted List
Easy

716

78

Favorite

Share
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        #go through all the numbers in the list
        while current:
            runner = current.next
         
            #while runner: current.next exist and the number is duplicated 
            #stay in the while loop until the number is different
            while runner and current.val == runner.val: 
                runner = runner.next
            #exit the loop when the number is different 
            runner.next = runner
            # when the number is different, the pointer of current will 
            #point to the following different number 
            current = runner 
        return head
        # we basically rewrite the linked list itself. so just return head
"""
Success
Details 
Runtime: 48 ms, faster than 85.04% of Python3 online submissions for Remove Duplicates from Sorted List.
Memory Usage: 13.2 MB, less than 5.26% of Python3 online submissions for Remove Duplicates from Sorted List.

"""
