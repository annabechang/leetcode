"""

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""



# TWO POINTERS
# TC : O(n)    
# SC : O(1) since we're not using any space to store anything        
# because the nums is sorted
# i starts at the begining of nums
# j starts at the end of nums
# add i and j
# if sum of i and j is smaller than target
# move i up
# otherwise move j down



class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        i = 0
        j = len(nums) -1
        nums = sorted(zip(nums, range(len(nums))))
        while i<j:
            s = nums[i][0]+nums[j][0]
            if s == target:
                return [nums[i][1],nums[j][1]]
            elif s < target:
                i+=1
            else:
                j-=1
                
        
"""
Details 
Runtime: 40 ms, faster than 75.69% of Python3 online submissions for Two Sum.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Two Sum.
"""
another option:        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i,v in enumerate(nums):
            rem = target - nums[i]

            if rem in seen:
                return[i, seen[rem]]

            else:
                seen[v] = i
                # print(seen)   
        
        
        
        
        
        
