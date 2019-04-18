"""
69. Sqrt(x)
Easy

707

1286

Favorite

Share
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
             
"""
class Solution:
    def mySqrt(self, x: int) -> int:
 
        if x < 2:
            return x
  
        left, right = 1, x // 2 
        
        while left <= right:
            mid = left + (right - left) // 2

            if mid > x/mid :
                #mid^2> x. righ is too big 
                right = mid -1
            else:
                left = mid + 1 
        # left > right
        return left - 1 

"""
Success
Details 
Runtime: 44 ms, faster than 94.76% of Python3 online submissions for Sqrt(x).
Memory Usage: 13.2 MB, less than 5.75% of Python3 online submissions for Sqrt(x).
"""



