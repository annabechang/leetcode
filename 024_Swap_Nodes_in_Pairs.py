"""
24. Swap Nodes in Pairs
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.

Explination:
we approach this problem by changing the links
so 
cur      1st   sec
dummy -> 1   -> 2   -> n

1. cur.next = sec
cur      1st   sec
dummy (x) 1   -> 2   -> n
  ------------->

2. first.next = sec.next

cur      1st   sec
dummy (x) 1  (x) 2   -> n
  ------------->
          ------------->

3. sec.next = first

cur      1st   sec
dummy (x) 1  (x) 2  (x) n
  ------------->
          ------------->
           <----
           
4. cur = cur.next.next
               cur
         sec   first
dummy  -> 2  -> 1    ->  n

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        while current.next and current.next.next:
            first=current.next
            second = current.next.next
            
            current.next = second
            first.next = second.next
            second.next = first
            
            current = current.next.next
        return dummy.next

"""
recursive
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            prev = head
            cur = head.next
            ahead = cur.next
            
            cur.next = prev
            prev.next = ahead
            
            prev.next = self.swapPairs(ahead)

            return cur
        return head

        






        
