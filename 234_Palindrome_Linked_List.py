"""
234. Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # initiate
        fast = slow = head
        stack = []
        
        while fast and fast.next:
            #find the middle point
            #save the first half into stack
            stack.append(slow.val)
            #update iteration
            slow = slow.next
            fast = fast.next.next
            #fast stop when there's no fast.next 
            #slow is stopped at the middle point
            # move the slow pointer passed the middle point 
        if fast:
            slow = slow.next 
        # while the second part still not finished yet 
        while stack:
            if stack.pop() != slow.val:
                return False
            slow = slow.next

        return True
"""
Success
Details 
Runtime: 80 ms, faster than 59.81% of Python3 online submissions for Palindrome Linked List.
Memory Usage: 24.6 MB, less than 7.40% of Python3 online submissions for Palindrome Linked List.
"""
