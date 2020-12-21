"""
383. Ransom Note
Easy

745

218

Add to List

Share
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

You may assume that both strings contain only lowercase letters.
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        chars = set(ransomNote)
        for x in chars:
            if ransomNote.count(x) > magazine.count(x):
                return False
        return True
"""
Success
Details 
Runtime: 36 ms, faster than 91.93% of Python3 online submissions for Ransom Note.
Memory Usage: 14.4 MB, less than 62.49% of Python3 online submissions for Ransom Note.
"""
