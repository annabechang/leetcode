"""
171. Excel Sheet Column Number

Easy

539

101

Favorite

Share
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
"""
class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0
        
        for i in range(len(s)):
            result *= 26
            result += ord(s[i])-ord('A') +1
        
        return result
"""
Success
Details 
Runtime: 36 ms, faster than 96.28% of Python3 online submissions for Excel Sheet Column Number.
Memory Usage: 13.2 MB, less than 71.31% of Python3 online submissions for Excel Sheet Column Number.

"""
