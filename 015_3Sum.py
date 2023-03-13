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


"""
two pointer method 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            
            if i>0 and nums[i-1] == nums[i]:
                continue
            
            l = i+1
            r = len(nums)-1
            # print(nums[i],nums[l],nums[r])
            while l<r:
                s = nums[i]+nums[l]+nums[r]
                # print(nums[i],nums[l],nums[r])
                if  s>0:
                    r-=1
                    # print("el2",nums[i],nums[l],nums[r])
                elif s < 0:
                    l+=1
                    # print("el1",nums[i],nums[l],nums[r])
                   
                
                else:
                    # s == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    #this while loop is to skip duplicates
                    while nums[l-1] == nums[l] and l<r:
                        l+=1
                    # print("el0",nums[i],nums[l],nums[r])
                    
                
        return res
        """
