"""
15. 3Sum
Medium

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        nums.sort()
        
        for i in range(n-2):
            #n-2 bec/ if i = n-2 ~ n, it's meaningless to set i to n-1 and n since there won't be enough numbers 
            # if i=0~ 2 > 0 means there's not enough - numbers
            if nums[i] + nums[i+1] + nums[i+2] > 0:
                break
            # if i = -100, -2 ~ 8,9 move from i = -100 to i = -2
            if nums[i] + nums[n-2] + nums[n-1] < 0:
                continue
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            l, r = i+1, n-1
            # it will break when l=r
            while l < r:
                tmp = nums[i] + nums[l] + nums[r]
                if tmp == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    #make sure you're getting different number
                    while l+1 < r and nums[l] == nums[l+1]:
                        l += 1
                    l +=1
                    while r-1 > l and nums[r] == nums[r-1]:
                        r -= 1
                    r -= 1
                elif tmp < 0:
                    l +=1
                else: 
                # tmp > 0:
                    r -= 1
        return result                       

"""
Success
Details 
Runtime: 736 ms, faster than 84.99% of Python3 online submissions for 3Sum.
Memory Usage: 17 MB, less than 27.86% of Python3 online submissions for 3Sum.

"""
