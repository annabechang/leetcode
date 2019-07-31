"""
242. Valid Anagram
Easy

778

114

Favorite

Share
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        dic = {}
        
        for i in s:
            if i not in dic:
                # add i into dictionary if not in 
                dic[i] = 1
            else:
                dic[i] += 1
        
        #now we can either:
        #create another dic and compare
        # - found in t
        
        for j in t:
            if j not in dic:
                return False
            else:
                dic[j] -= 1
                
        for k in dic:
            if dic[k]!=0:
                return False
        return True
"""
Success
Details 
Runtime: 52 ms, faster than 78.93% of Python3 online submissions for Valid Anagram.
Memory Usage: 14.2 MB, less than 7.85% of Python3 online submissions for Valid Anagram.

"""
