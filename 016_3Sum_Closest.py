"""
16. 3Sum Closest
Medium

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        result = nums[0] + nums[1] + nums[n-1]
        nums.sort()
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i+1, n-1
            while l < r:
                tmp = nums[i]+nums[l]+nums[r]
                if abs(result - target) > abs(tmp - target):
                    result = tmp
                    # tmp is closer to target 
                    
                if tmp == target:
                    return target
                
                elif tmp < target:
                    l +=1
                else:
                    # tmp > target
                    r -= 1
                    
        return result
                
                    
"""
Success
Details 
Runtime: 112 ms, faster than 84.63% of Python3 online submissions for 3Sum Closest.
Memory Usage: 13.9 MB, less than 5.41% of Python3 online submissions for 3Sum Closest.
"""
