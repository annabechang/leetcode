"""
237. Delete Node in a Linked List
Easy

804

3864

Favorite

Share
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Given linked list -- head = [4,5,1,9], which looks like following:



 

Example 1:

Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
Example 2:

Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.
 

Note:

The linked list will have at least two elements.
All of the nodes' values will be unique.
The given node will not be the tail and it will always be a valid node of the linked list.
Do not return anything from your function.

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
"""
Success
Details 
Runtime: 48 ms, faster than 48.33% of Python3 online submissions for Delete Node in a Linked List.
Memory Usage: 14.2 MB, less than 6.04% of Python3 online submissions for Delete Node in a Linked List.
"""

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        current = node
        while node.next != None:
            node.val = node.next.val
            current = node
            node = node.next
        current.next = None
"""
Success
Details 
Runtime: 44 ms, faster than 79.17% of Python3 online submissions for Delete Node in a Linked List.
Memory Usage: 13.9 MB, less than 6.04% of Python3 online submissions for Delete Node in a Linked List.
"""
