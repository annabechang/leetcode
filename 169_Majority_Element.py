"""
169. Majority Element

Easy

1638

142

Favorite

Share
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""
#Boyer–Moore majority vote
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        index, count = 0, 1
        
        for i in range(1,len(nums)):
            if nums[index] == nums[i]:
                count += 1
            else:
                count -= 1
                if count == 0:
                    index = i
                    count = 1
        return nums[index]
        
"""
Success
Details 
Runtime: 48 ms, faster than 85.97% of Python3 online submissions for Majority Element.
Memory Usage: 14.2 MB, less than 84.55% of Python3 online submissions for Majority Element.
"""

#divide and conquer
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        
        mid = len(nums) // 2
        l = self.majorityElement(nums[:mid])
        r = self.majorityElement(nums[mid:])
        
        if l == r:
            return l 
        
        return [r,l][nums.count(l) > mid]

"""
Success
Details 
Runtime: 140 ms, faster than 5.22% of Python3 online submissions for Majority Element.
Memory Usage: 14.3 MB, less than 53.71% of Python3 online submissions for Majority Element.


"""
