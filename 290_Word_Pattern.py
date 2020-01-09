"""
290. Word Pattern
Easy

857

120

Add to List

Share
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.


"""
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        word = str.split(' ')
        
        #if number doesn't match
        
        if len(word) != len(pattern):
            return False
        
        #build hash map 
        hashmap = {}
        mapval = {}
        
        for i in range(len(pattern)):
            if pattern[i] in hashmap:
                if hashmap[pattern[i]] != word[i]:
                    return False
            
            else: #if not in hashmap, have the value appeared in the string before
                if word[i] in mapval:
                    return False
            #add pattern i and word i to hashmap
            hashmap[pattern[i]] = word[i]
            # add words into map value 
            mapval[word[i]] = True
        
        return True
"""
Success
Details 
Runtime: 24 ms, faster than 85.88% of Python3 online submissions for Word Pattern.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Word Pattern.
"""
