"""
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non decreasing array.
-10^9 <= target <= 10^9
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1
        
        while l<=r:
            m = (l+r)//2
            if nums[l] == nums[r] == target:
                return [l,r]
            elif target < nums[m]:
                r=m-1
            elif target > nums[m]:
                l=m+1
            else:
                if nums[l]!= target:
                    l+=1
                if nums[r]!=target:
                    r-=1

        return [-1,-1]

"""
Runtime: 76 ms, faster than 99.36% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
Memory Usage: 15.2 MB, less than 31.86% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
"""

