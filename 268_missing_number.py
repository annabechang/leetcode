"""
268. Missing Number
Easy

1104

1508

Favorite

Share
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        num_sum = sum(nums)
        remain = (0+n)*(n+1)/2 - num_sum 
        
        
        return int(remain)
"""
Success
Details 
Runtime: 156 ms, faster than 68.58% of Python3 online submissions for Missing Number.
Memory Usage: 15 MB, less than 6.45% of Python3 online submissions for Missing Number.
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        for i in range(n):
            n = n^i^nums[i-1]
        return n
    

"""
Success
Details 
Runtime: 168 ms, faster than 26.04% of Python3 online submissions for Missing Number.
Memory Usage: 15 MB, less than 6.45% of Python3 online submissions for Missing Number.
"""
"""class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # tmp_max = max(nums)
        # while len(nums)>0:
        #     keep_max = max(nums)
        #     diff = tmp_max - keep_max
            
        #     if diff ==1:
        #         nums.remove(keep_max)
        # return keep_max
        # binary solution below using xor (01 -> 1)
        # res = len(nums)

        # for i in range(len(nums)):
        #     print(i,res,nums[i])
        #     res=res+(i - nums[i])
        #     print(i,res,nums[i])
        # return res

        #用等差數列
        n = len(nums)
        sum = n*(n+1)/2
        for i in nums:
            sum-= i
        return int(sum)

"""
