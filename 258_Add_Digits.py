"""
258. Add Digits
Easy

489

818

Favorite

Share
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""
class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            num = sum(int(c) for c in str(num))
        return num
"""
Success
Details 
Runtime: 40 ms, faster than 54.85% of Python3 online submissions for Add Digits.
Memory Usage: 14 MB, less than 5.26% of Python3 online submissions for Add Digits.
"""
"""
when input: 10 - ... more
output : 10 = 1+0 = 1, 1+1=2 ... 1+8=9, 1+9 = 10 = 1, 2+0=2....
our output has a relationship with 9. when number - 1 is a multiple of 9, like [(10 - 1= 9)% 9 = 0] +1 = 1
another example: input38: 38-1 = 37, 37 mod 9 = 1, 1+1 = 2 == (3+8)=11, 1+1 = 2
"""
class Solution:
    def addDigits(self, num: int) -> int:
        if num <= 0:
            return 0
        
        else:
            result = (num -1) % 9 +1 
        
        return result

"""
Success
Details 
Runtime: 36 ms, faster than 82.11% of Python3 online submissions for Add Digits.
Memory Usage: 13.9 MB, less than 5.26% of Python3 online submissions for Add Digits.
Next challenges:
"""
