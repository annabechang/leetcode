"""
14. Longest Common Prefix
Easy

1166

1191

Favorite

Share
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        for i in range(len(strs[0])):
            #if str[0[i]] = str[1][i] and compare to all the following
            for string in strs[1:]:
                if i >= len(string) or string[i] != strs[0][i] :
                    return strs[0][:i]
                # if i >= len(string) i.e. flow is shorter than flower
        return strs[0]
        
"""
Success
Details 
Runtime: 56 ms, faster than 24.24% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 13 MB, less than 5.10% of Python3 online submissions for Longest Common Prefix.
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        i = 0
        
        while True:
            try:
                # set function will return the unique found value 
                sets = set(string[i] for string in strs)
                if len(sets) == 1:
                    result += sets.pop()
                    i += 1
                else: break
            except Exception as e:
                break
        return result


"""
Success
Details 
Runtime: 44 ms, faster than 47.69% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 13.3 MB, less than 5.10% of Python3 online submissions for Longest Common Prefix.
"""



        
        
