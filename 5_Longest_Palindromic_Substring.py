"""
5. Longest Palindromic Substring
Medium

3782

359

Favorite

Share
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

"""
        # two different situation: central symmetry, symmetry by itself 
        # B
        # ABA
        # CABAC
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        palindrome = ''
        
        for i in range(len(s)):
            len1 = len(self.getlongestPalindrome(s,i,i))
            if len1 > len(palindrome):
                palindrome = (self.getlongestPalindrome(s,i,i))
                
            len2 = len(self.getlongestPalindrome(s,i,i+1))
            
            if len2 > len(palindrome):
                palindrome = (self.getlongestPalindrome(s,i,i+1))    
    
        return palindrome 



        # continue while the considtion is satisfied 
        # left >= 0 and right < len(s) : if it's out of range
        # if it's symmetry like bab -> cbabc 
        
      def getlongestPalindrome(self, s, left, right):

          while left >= 0 and right < len(s) and s[left] == s[right]:
              left -= 1
              right += 1
          return s[left+1 : right]
"""

Success
Details 
Runtime: 1188 ms, faster than 47.04% of Python online submissions for Longest Palindromic Substring.
Memory Usage: 11.8 MB, less than 63.12% of Python online submissions for Longest Palindromic Substring.

"""
