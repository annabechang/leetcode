"""
108. Convert Sorted Array to Binary Search Tree

Easy

1077

106

Favorite

Share
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""

"""
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        
        mid = len(nums) // 2
        
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        return root

Success
Details 
Runtime: 64 ms, faster than 88.22% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
Memory Usage: 15.5 MB, less than 5.70% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.

"""
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
 
        def to_bst(nums, start, end):
            if start > end:
                return None

            mid = (start + end) // 2
            node = TreeNode(nums[mid])
            node.left = to_bst(nums, start, mid-1)
            node.right = to_bst(nums, mid+1, end)
            return node
        
        return to_bst(nums, 0, len(nums)-1)
"""
Success
Details 
Runtime: 64 ms, faster than 88.22% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
Memory Usage: 15.6 MB, less than 5.70% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
"""
