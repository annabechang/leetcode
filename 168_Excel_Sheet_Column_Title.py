"""
168. Excel Sheet Column Title

Easy

706

140

Favorite

Share
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
"""
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result, num = "", n
        
        while num:
            result += chr((num -1) % 26 +ord('A'))
            num = (num -1) // 26
        
        return result[::-1] 
"""
Success
Details 
Runtime: 20 ms, faster than 64.74% of Python online submissions for Excel Sheet Column Title.
Memory Usage: 11.5 MB, less than 97.29% of Python online submissions for Excel Sheet Column Title.

"""
