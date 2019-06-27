"""
3. Longest Substring Without Repeating Characters

Medium

5707

324

Favorite

Share
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
# BUILD A DICTIONARY 
# dict = {"a":1, "b":2 ... }
# we need a start pointer 
# what if start is empty -> expected output = 1
# max = i - start = 0 -> i - 1 = -1

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = -1
        max_sub = 0
        dic = {}
        
        for i in range(len(s)):
            #s[i] in dic -> update start and dictionary 
            if s[i] in dic and dic[s[i]] > start:
                start = dic[s[i]]
                dic[s[i]] = i
                
            #s[i] not in dic -> add it to dict
            else:
                dic[s[i]] = i
                # if we found a longer substring, update max substring lenth
                if i - start > max_sub:
                    max_sub = i - start 
                    
        return max_sub
"""
Success
Details 
Runtime: 32 ms, faster than 98.21% of Python online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 12.7 MB, less than 26.48% of Python online submissions for Longest Substring Without Repeating Characters.

"""
