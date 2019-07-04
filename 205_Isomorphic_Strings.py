"""
205. Isomorphic Strings
Easy

776

225

Favorite

Share
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
"""
"""
we need 2 dictionary, here's why:
take Example 2:

Input: s = "foo", t = "bar"
Output: false

#1 dictionary_s:
s = 'foo'
dict={}

s[0] = 'f'
doct={'f':'b'}

s[1] = 'o'
doct={'f':'b', 'o':'a'}

s[2] = 'o'
-> return false

#2 dictionary_t:
t = 'bar'
dict={}

t[0] = 'b'
doct={'b':'f'}

t[1] = 'a'
doct={'b':'f', 'a':'o'}

t[2] = 'r'
doct={'b':'f', 'a':'o','r':'o'}

-> return True
==> result False

"""
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        return self.halfIso(s,t) and self.halfIso(t,s)
    
    def halfIso(self, s, t):
        lookup_dic = {}
        for i in range(len(s)):
            if s[i] not in lookup_dic:
                lookup_dic[s[i]] = t[i]
            elif lookup_dic[s[i]] != t[i]:
                return False
        return True



"""
Success
Details 
Runtime: 32 ms, faster than 69.08% of Python online submissions for Isomorphic Strings.
Memory Usage: 13.1 MB, less than 52.79% of Python online submissions for Isomorphic Strings.
"""
