"""
125. Valid Palindrome
Easy

574

1685

Favorite

Share
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
      #palindrom means it's the same going forward and backward. thus we have a pointer start from the beg
      # and another pointer start from the back
        i, j = 0,(len(s)-1)
        
        while i < j:
        #we check if i is a valid alphanumeric. if it's space or ,. etc we will ignore it
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            else:
                if s[i].lower() != s[j].lower():
                    return False
                else:
                    i += 1 
                    j -= 1
                
        return True
                        
                
"""
Success
Details 
Runtime: 72 ms, faster than 34.51% of Python3 online submissions for Valid Palindrome.
Memory Usage: 13.3 MB, less than 73.19% of Python3 online submissions for Valid Palindrome.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(e for e in s if e.isalnum()).lower()
        return s == s[::-1]
"""
Details 
Runtime: 48 ms, faster than 96.24% of Python3 online submissions for Valid Palindrome.
Memory Usage: 14 MB, less than 41.35% of Python3 online submissions for Valid Palindrome.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0,(len(s)-1)
        
        while i < j:
            while i<j and not s[i].isalnum():
                i += 1
            while i<j and not s[j].isalnum():
                j -= 1
      
            if s[i].lower() != s[j].lower():
                return False
            else:
                i += 1 
                j -= 1
                
        return True
                        
"""
Success
Details 
Runtime: 60 ms, faster than 75.19% of Python3 online submissions for Valid Palindrome.
Memory Usage: 13.4 MB, less than 66.02% of Python3 online submissions for Valid Palindrome.
"""
