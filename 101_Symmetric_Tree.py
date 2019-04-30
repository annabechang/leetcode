"""
101. Symmetric Tree
Easy

2111

45

Favorite

Share
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.isSymmetricRecurrent(root.left, root.right)
    
    def isSymmetricRecurrent(self, left, right):
        if left is None and right is None:
            return True
        
        if left is None or right is None or left.val != right.val:
            return False
        
        return self.isSymmetricRecurrent(left.left, right.right) and self.isSymmetricRecurrent(left.right, right.left)
            
"""
Success
Details 
Runtime: 40 ms, faster than 99.16% of Python3 online submissions for Symmetric Tree.
Memory Usage: 13.2 MB, less than 5.61% of Python3 online submissions for Symmetric Tree.
"""
