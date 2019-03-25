"""
28. Implement strStr()
Easy

793

1224

Favorite

Share
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle)+1):
           if haystack[i:i+len(needle)] == needle:
            return i
        else:
            return -1
            
"""
 Success
Details 
Runtime: 40 ms, faster than 59.53% of Python3 online submissions for Implement strStr().
Memory Usage: 13.3 MB, less than 5.13% of Python3 online submissions for Implement strStr()."""
