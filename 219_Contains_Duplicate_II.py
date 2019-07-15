"""
219. Contains Duplicate II
Easy

524

645

Favorite

Share
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        dic = {}
        
        for i, num in enumerate(nums):
            if num not in dic:
                dic[num] = i
                # i = index
            else:
                # i = current index. dic[num]: the index apprears previously
                if i - dic[num] <= k:
                    return True
                #if it didn't finds it, update the index to current 
                # for cases like [1,0,1,1]
                dic[num] = i
                
        return False
                

"""
Success
Details 
Runtime: 84 ms, faster than 37.37% of Python online submissions for Contains Duplicate II.
Memory Usage: 16.2 MB, less than 61.79% of Python online submissions for Contains Duplicate II.
"""
