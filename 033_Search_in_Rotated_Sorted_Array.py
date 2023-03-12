"""
33. Search in Rotated Sorted Array
Medium

3673

400

Add to List

Share
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1


Explanation

Let's say nums looks like this: [12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

Because it's not fully sorted, we can't do normal binary search. But here comes the trick:

If target is let's say 14, then we adjust nums to this, where "inf" means infinity:
[12, 13, 14, 15, 16, 17, 18, 19, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]

If target is let's say 7, then we adjust nums to this:
[-inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

And then we can simply do ordinary binary search.

idea credit to:https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14435/Clever-idea-making-it-simple 


"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)
        
        while low < high:
            mid = (low+high)//2
            
            if target < nums[0] < nums[mid]: #-inf
                low = mid+1
            
            elif target>=nums[0]>nums[mid]: #+inf
                high = mid   
                
            elif (nums[mid] < target):
                low = mid+1
                
            elif (nums[mid] > target) :
                high = mid
           
            else:
                return mid
        return -1

"""
Success
Details 
Runtime: 40 ms, faster than 67.67% of Python3 online submissions for Search in Rotated Sorted Array.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Search in Rotated Sorted Array.
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)
        
        while low < high:
            mid = (low+high)//2
            
            num = nums[mid] if (nums[mid] < nums[0]) == (target < nums[0]) else (-math.inf if target < nums[0] else math.inf)
            
                
            if (num < target):
                low = mid+1
                
            elif (num > target) :
                high = mid
           
            else:
                return mid
        return -1
"""
Success
Details 
Runtime: 28 ms, faster than 99.35% of Python3 online submissions for Search in Rotated Sorted Array.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Search in Rotated Sorted Array.
"""

"""
list all the possible situations when do we need to move the left pointer etc 
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l<=r:
            m = (l+r)//2
            # print(l,m,r)
            print(nums[l],nums[m],nums[r])

            if nums[m] == target:
                return m
            

            elif target>nums[m]>=nums[l] or nums[m]>=nums[l]>target or nums[l]>target>nums[m]:
                # the = here is to capture the edge case when there's only 2 element in the nums. 
                l = m+1
                # print(nums[l],nums[m],nums[r])
            else:
                r = m-1
            print(l,m,r)
            
        return -1

"""

