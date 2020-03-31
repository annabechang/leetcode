"""
345. Reverse Vowels of a String
Easy

558

1002

Add to List

Share
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        vow = "aeiou"
        string = list(s)
        i,j = 0, len(s)-1
        
        while i < j:
            if string[i].lower() not in vow:
                i+=1
            elif string[j].lower() not in vow:
                j-=1
            else:
                string[i],string[j] = string[j], string[i]
                i+=1
                j-=1
        return "".join(string)
                
"""
Runtime: 56 ms, faster than 56.66% of Python3 online submissions for Reverse Vowels of a String.
Memory Usage: 14.8 MB, less than 6.67% of Python3 online submissions for Reverse Vowels of a String.
"""
