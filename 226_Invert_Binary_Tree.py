"""
226. Invert Binary Tree
Easy

1815

30

Favorite

Share
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is not None:
            root.left, root.right = self.invertTree( root.right), self.invertTree(root.left)
        return root 
"""
Success
Details 
Runtime: 32 ms, faster than 88.15% of Python3 online submissions for Invert Binary Tree.
Memory Usage: 13.2 MB, less than 53.53% of Python3 online submissions for Invert Binary Tree.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        #edge
        if not root:
            return 
        
        #swap
        temp = root.left
        root.left = root.right
        root.right = temp
        
        #recursion
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root 

"""
Success
Details 
Runtime: 36 ms, faster than 64.95% of Python3 online submissions for Invert Binary Tree.
Memory Usage: 13.2 MB, less than 26.71% of Python3 online submissions for Invert Binary Tree.

"""
