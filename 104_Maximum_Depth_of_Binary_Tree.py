"""
104. Maximum Depth of Binary Tree
Easy

1250

48

Favorite

Share
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.


"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        
    
            
"""
Success
Details 
Runtime: 48 ms, faster than 88.50% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 15.5 MB, less than 5.13% of Python3 online submissions for Maximum Depth of Binary Tree.
"""
