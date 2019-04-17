"""
67. Add Binary
Easy

893

179

Favorite

Share
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result, carry, val = "", 0, 9
        for i in range(max(len(a), len(b))):
            val = carry 
            if i<len(a):
                val += int(a[-(i+1)])
                
            if i <len(b):
                val += int(b[-(i+1)])
            
            carry, val = val // 2, val % 2 
            result += str(val)
        
        if carry:
            result += str(1)
        return result[::-1]
"""
Success
Details 
Runtime: 44 ms, faster than 80.55% of Python3 online submissions for Add Binary.
Memory Usage: 13.2 MB, less than 5.43% of Python3 online submissions for Add Binary.
"""
