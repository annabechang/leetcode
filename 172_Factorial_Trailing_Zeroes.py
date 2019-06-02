"""
172. Factorial Trailing Zeroes

Easy

474

675

Favorite

Share
Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.
"""
class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 0
        
        while n != 0:
            result += n // 5
            n = n // 5
        return result 
 
"""
Success
Details 
Runtime: 36 ms, faster than 89.48% of Python3 online submissions for Factorial Trailing Zeroes.
Memory Usage: 13.4 MB, less than 5.38% of Python3 online submissions for Factorial Trailing Zeroes.

 """
