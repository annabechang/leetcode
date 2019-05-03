"""
107. Binary Tree Level Order Traversal II
Easy

699

130

Favorite

Share
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
        result, current =[],[root]
        while current:
            next_level, vals = [], []
            for node in current:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current = next_level
            result.append(vals)
            #result: [3],[9,20],[15,7] --> [::-1]
            
        return result[::-1]
"""
Success
Details 
Runtime: 40 ms, faster than 98.23% of Python3 online submissions for Binary Tree Level Order Traversal II.
Memory Usage: 13.2 MB, less than 26.18% of Python3 online submissions for Binary Tree Level Order Traversal II.
"""
