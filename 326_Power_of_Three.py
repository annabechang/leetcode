"""
326. Power of Three
Easy

424

1346

Add to List

Share
Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false
Example 3:

Input: 9
Output: true
Example 4:

Input: 45
Output: false
Follow up:
Could you do it without using any loop / recursion?
"""
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        elif n <=2:
            return False
        while n>3:
            if n%3 == 0:
                n/=3
            else:
                return False 
        if n == 3:
            return True
        else:
            return False 
"""
64 ms	12.8 MB
"""
