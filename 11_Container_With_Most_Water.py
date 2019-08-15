"""
11. Container With Most Water
Medium
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49

"""
# use left and right pointer

class Solution:
    def maxArea(self, height: List[int]) -> int:
        #init
        left, right = 0, len(height) -1
        #result = max area of water contained
        result = 0
        
        while left < right:
            #water is the area contained everytime
            # find the minimum and calculate the area
            water = min(height[left], height[right]) *(right-left)
            
            #update result
            if water > result:
                result = water
            
            # we decide to move the left or right pointer based on
            # which one is smaller 
            # we try to keep the bigger one in order to get max result
            elif height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return result 
"""
Success
Details 
Runtime: 136 ms, faster than 89.48% of Python3 online submissions for Container With Most Water.
Memory Usage: 15.5 MB, less than 5.26% of Python3 online submissions for Container With Most Water.

"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j = 0, len(height) -1
        area = []

        while i != j:
            if height[i] < height[j]:
                area.append(height[i]*(j-i))
                i += 1
            else:
                area.append(height[j]*(j-i))
                j -= 1
        return max(area)
"""
Success
Details 
Runtime: 140 ms, faster than 78.14% of Python3 online submissions for Container With Most Water.
Memory Usage: 15.5 MB, less than 5.26% of Python3 online submissions for Container With Most Water.
"""


