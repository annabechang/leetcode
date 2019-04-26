"""
100. Same Tree
Easy

1079

32

Favorite

Share
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        #when p = q = none
        if p is None and q is None:
            return True
        
        #when p and q != none 
        if p is not None and q is not None:
        #p.q has same value, p.q's left tree has same val
        #pq's right tree has same val
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right,q.right)
        
        # if p = none & q !=None or p!=None & q=None
        return False
"""
Success
Details 
Runtime: 36 ms, faster than 82.52% of Python3 online submissions for Same Tree.
Memory Usage: 13.2 MB, less than 5.74% of Python3 online submissions for Same Tree.
"""
