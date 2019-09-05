"""
18. 4Sum
Medium

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""
# the main idea for 4 sun is as the following:
# 4 sum = i + 3 sum
# j == i + 1 then the problem become 4 sum = i + j + 2 sum

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        result = []
        nums.sort()
        
        # loop for first num, n times at 4 sum level
        for i in range(n-3):
            # skip uneccesary case
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
                
            # skip uneccesary case
            if nums[i] + nums[n-1] + nums[n-2] + nums[n-3] < target:
                continue
            
            # skip duplication     
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # loop for second number, n times at 3 sum level
            for j in range(i + 1, len(nums) - 2):
                # skip duplication
                if j != i +1 and nums[j] == nums[j-1]:
                    continue
                # skip uneccesary case
                if nums[j]+nums[j+1]+nums[j+2] > target - nums[i]:
                    break
                    
                # search for last 2 nums, same as 2Sum problem using 2 pointer lef and right    
                l, r = j+1, n-1
                
                while l < r: 
                    
                    tmp = nums[i] + nums[j] + nums[l] + nums[r]

                    if tmp > target:
                        r -= 1
                    elif tmp < target:
                        l +=1
                    else: 
                    # when tmp == target
                        result.append([nums[i], nums[j] , nums[l] , nums[r]])
                        # skip duplication
                        while r > l and nums[l] == nums[l+1]:
                            l +=1
                        while r > l and nums[r] == nums[r-1]:
                            r -=1
                        skip duplication and increment
                        l, r = l + 1, r - 1
        return result 
                                   
"""
Success
Details 
Runtime: 88 ms, faster than 95.57% of Python3 online submissions for 4Sum.
Memory Usage: 13.7 MB, less than 7.14% of Python3 online submissions for 4Sum.

"""
 
