"""
35. Search Insert Position
Easy

1195

167

Favorite

Share
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #there's no reason to go through the array if it can simply be inserted to the end 
        if target > nums[len(nums)-1]:
            return len(nums)
        
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
                
"""
Details 
Runtime: 36 ms, faster than 91.69% of Python3 online submissions for Search Insert Position.
Memory Usage: 13.8 MB, less than 5.11% of Python3 online submissions for Search Insert Position.
"""
