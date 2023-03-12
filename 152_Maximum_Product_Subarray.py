"""
152. Maximum Product Subarray
Medium
15.4K
465
Companies
Given an integer array nums, find a 
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        max_pro = nums[0]
        min_pro = nums[0]
        result = nums[0]
        for i in range(1,len(nums)):
            tmp = max_pro
            max_pro = max(tmp*nums[i], min_pro*nums[i],nums[i])
            # if tmp_max > max_pro:
                # max_pro = tmp_max 
            min_pro = min(tmp*nums[i], min_pro*nums[i],nums[i])
            # if tmp_min < min_pro:
                # min_pro = tmp_min 
            
            result = max(max_pro, result)
            print(i, min_pro, max_pro, result)
        return result
