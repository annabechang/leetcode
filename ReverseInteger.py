"""
7. Reverse Integer 
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

class Solution:
    def reverse(self, x: 'int') -> 'int':
        # 1. get absolute value of x
        # 2. convert to string
        # 3. reverse ->string
        # 4. convert to int
        # 5. verify if x is greater than 0 or less than 0
        # [1,-1][x < 0] means if x< 0 is true:
        # if true , sign = 1. if false, sign = -1
        # 6. return total value of reverse times sign 
        # 7. consider if total is in the range limit 
        
        rev = int(str(abs(x))[::-1])
        sign = [1,-1][x < 0]
        total = rev*sign
        return total if (-2**31) <= total <= (2**31 -1) else 0


"""
Success
Details 
Runtime: 48 ms, faster than 100.00% of Python3 online submissions for Reverse Integer.
Memory Usage: 12.7 MB, less than 19.52% of Python3 online submissions for Reverse Integer.

"""
