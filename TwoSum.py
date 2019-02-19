"""

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""


#Bruet Force Solution
#Time complexity: O(n^2)
#Space complexity: O(1)
"""
class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    print (nums[i], nums[j])
                return True
        return False
        
"""


#Hashtable
#TC: O(n)
#SC: O(n)
#add each element in array to a hashtable
#weather the target - the element is present in the hashtable
# for example:
# nums = [2,4,6]
# target = 10
# 
# i=0
# ht = dict()
# ht[10 - 2] = ht[8] = 2

# i = 1
# ht[10 - 4] = ht [6] = 4

#i = 2
# ht[6] already exist. return the value 4 => sum the target value
"""
class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        ht = dict()
        for i in range(len(nums)):
            if nums[i] in ht:
                print(ht[nums[i]], nums[i])
                return True
            else:
                ht[target - nums[i]] = nums[i]
                
        return False
"""        
# TWO POINTERS
# TC : O(n)    
# SC : O(1) since we're not using any space to store anything        
# because the nums is sorted
# i starts at the behining of nums
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
        
        
        
        
        
        
        
        
