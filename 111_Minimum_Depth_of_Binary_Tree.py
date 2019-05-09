"""
111. Minimum Depth of Binary Tree

Easy

691

369

Favorite

Share
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        # we need to make sure left and right child exist first, otherwise if it's not there and we +1 it'll not be correct 
        
        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        
        else: 
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
"""
Success
Details 
Runtime: 52 ms, faster than 74.83% of Python3 online submissions for Minimum Depth of Binary Tree.
Memory Usage: 15.5 MB, less than 6.33% of Python3 online submissions for Minimum Depth of Binary Tree.
"""
