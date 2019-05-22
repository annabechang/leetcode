"""
136. Single Number
Easy

2387

91

Favorite

Share
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        dict = {}
        
        for num in nums:
#            if num in dict:
#                dict[num] +=1
#            else:
#                dict[num] = 1
            dict[num] = dict.get(num, 0) +1 
        
        for key, val in dict.items():
            if val == 1 :
                return key

"""
Success
Details 
Runtime: 48 ms, faster than 44.58% of Python3 online submissions for Single Number.
Memory Usage: 15.1 MB, less than 16.96% of Python3 online submissions for Single Number.
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        
        for num in nums:
            ans ^= num     #XOR only 00 11 will return 0
            
        return ans
"""
Success
Details 
Runtime: 40 ms, faster than 94.00% of Python3 online submissions for Single Number.
Memory Usage: 14.7 MB, less than 57.75% of Python3 online submissions for Single Number.
"""
