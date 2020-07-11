"""
349. Intersection of Two Arrays
Easy

830

1221

Add to List

Share
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
"""
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersection(nums2,nums1) # use num 2 as base 
        
        lookup = set() # lookup table
        for i in nums1:
            lookup.add(i)
            
        result = []
        for i in nums2:
            if i in lookup:
                result += i,
                lookup.discard(i)
        return result 
"""
Success
Details 
Runtime: 60 ms, faster than 36.37% of Python3 online submissions for Intersection of Two Arrays.
Memory Usage: 14.1 MB, less than 11.94% of Python3 online submissions for Intersection of Two Arrays.

"""
