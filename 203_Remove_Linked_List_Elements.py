"""
203. Remove Linked List Elements

Easy

837

50

Favorite

Share
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        #dummy is the pointer always at the head so when we return it will start from head
        dummy = ListNode(float('-inf'))
        dummy.next = head
        previous, current = dummy, dummy.next
        
        while current:
            if current.val == val :
                previous.next = current.next
            else:
                previous = current
            current = current.next
        
        return dummy.next
        #return dummy.next instead of head to avoide situations when val = head then head does not exist 
"""
Success
Details 
Runtime: 48 ms, faster than 98.78% of Python online submissions for Remove Linked List Elements.
Memory Usage: 18.6 MB, less than 84.34% of Python online submissions for Remove Linked List Elements.
"""
