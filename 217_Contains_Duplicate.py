"""
217. Contains Duplicate
Easy

423

529

Favorite

Share
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""
# dictionary
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        diction = {}
        
        for i in nums:
            if i in diction:
                return True
            diction[i] = 1
        return False
"""
Success
Details 
Runtime: 108 ms, faster than 67.35% of Python online submissions for Contains Duplicate.
Memory Usage: 17.8 MB, less than 11.67% of Python online submissions for Contains Duplicate.
"""
#sort 
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return False
        else:

            nums.sort()
            for i in range(len(nums) - 1):
                if nums[i] == nums[i+1]:
                    return True
            return False 
"""
Success
Details 
Runtime: 112 ms, faster than 44.71% of Python online submissions for Contains Duplicate.
Memory Usage: 15.7 MB, less than 93.76% of Python online submissions for Contains Duplicate.
"""
# SOL
        # nums.sort()
        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return True
        # return False
# SOL
        # map = {}
        # for num in nums:
        #     if num in map:
        #         return True
        #     map[num] = True
        # # print(map)
        # return False
# SOL
#         uni = set(nums)
#         if len(nums) == len(uni):
#             return  False
#         return True
