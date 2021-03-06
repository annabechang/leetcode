"""
110. Balanced Binary Tree
Easy

1179

101

Favorite

Share
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        #to know left hight and right hight
        def get_height(root):
            if root is None:
                return 0
            
            left_height, right_height = get_height(root.left), get_height(root.right)
            
            #when would we return true/ false
            
            #if left_height != height balanced binary tree or right_height != hbbt or abs(left_height - right_height) > 1 -> return false
            
            if left_height < 0 or right_height < 0 or abs(left_height - right_height) > 1: 
                return -1
            # +1 root 
            return max(left_height, right_height) +1

        return (get_height(root) >= 0)
"""
Success
Details 
Runtime: 56 ms, faster than 99.72% of Python3 online submissions for Balanced Binary Tree.
Memory Usage: 18.9 MB, less than 5.41% of Python3 online submissions for Balanced Binary Tree.

"""
