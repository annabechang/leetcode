"""
206. Reverse Linked List
Easy

2457

65

Favorite

Share
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
"""
Iterative 

prev, current, next_pointer = None, head, None
prev  cur  
 x    1 -> 2 -> 3 -> x

next_pointer = current.next
prev  cur  next
 x    1 -> 2 -> 3 -> x

current.next = prev
prev  cur  next
 x  <- 1    2 -> 3 -> x

prev = current
current = next_pointer
     prev  cur
           next
 x  <- 1    2 -> 3 -> x

next_pointer = current.next
     prev  cur  next
 x  <- 1    2 -> 3 -> x

current.next = prev
     prev  cur  next
 x  <- 1 <- 2    3 -> x
 
 #advance
prev = current
current = next_pointer
          prev  cur  
                next
 x  <- 1 <- 2    3 -> x 
 
 next_pointer = current.next
           prev  cur  next
 x  <- 1 <- 2    3 -> x 
 
 current.next = prev
            prev    cur  next
 x  <- 1 <-   2  <-  3     x 
 
 #advance
prev = current
current = next_pointer
                   prev    cur
                          next
 x  <- 1 <-   2  <-  3     x  
 
return prev
3 -> 2 -> 1-> x

O(n) time 
O(1) space 
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #init pointers
        prev, current, next_pointer = None, head, None
        
        while current:
            #save next
            next_pointer = current.next
            #reverse
            current.next = prev
            #advance
            prev = current
            current = next_pointer
        return prev
"""
Success
Details 
Runtime: 24 ms, faster than 75.65% of Python online submissions for Reverse Linked List.
Memory Usage: 13.6 MB, less than 68.43% of Python online submissions for Reverse Linked List.
"""
"""
Recursive
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        #return me a reversed list, go down to the the last node in the list return itself 
        reversedListHead = self.reverseList(head.next)
        # recursion return upwards, as we go up each node, add itself to the reversed list While passing the list head up and up 
        head.next.next = head
        head.next = None
        #return the head 
        return reversedListHead
"""
Success
Details 
Runtime: 40 ms, faster than 80.27% of Python3 online submissions for Reverse Linked List.
Memory Usage: 18.9 MB, less than 15.23% of Python3 online submissions for Reverse Linked List.
"""



