"""
58. Length of Last Word
Easy

345

1437

Favorite

Share
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        local_count = 0 
        for i in range(len(s)):
            if s[i] == " ":
                local_count = 0
                #it's the end or it has a new word
            else: 
                local_count +=1 
                count = local_count
        return count
"""
Success
Details 
Runtime: 40 ms, faster than 27.29% of Python3 online submissions for Length of Last Word.
Memory Usage: 13.2 MB, less than 6.04% of Python3 online submissions for Length of Last Word.
"""   
