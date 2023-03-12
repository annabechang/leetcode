"""
53. Maximum Subarray
Easy

3940

134

Favorite

Share
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)
        
        local_max, global_max = 0,0
        
        for num in nums:
            local_max = max(num, local_max + num)  #ex at index 1, we compare 1 v.s. -2+1= -1 -> 1 
            global_max = max(global_max, local_max) # ex at index 2, we compare 0 v.s. 1 ->1 
        
        return global_max
        
"""
Success
Details 
Runtime: 44 ms, faster than 93.75% of Python3 online submissions for Maximum Subarray.
Memory Usage: 13.6 MB, less than 5.50% of Python3 online submissions for Maximum Subarray.
"""
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_so_far = nums[0]
        max_tmp = 0
        for i in range(len(nums)):

            max_tmp += nums[i]
            if max_tmp >= max_so_far:
                max_so_far = max_tmp
            if max_tmp < 0:
                max_tmp = 0
        return max_so_far
        """
