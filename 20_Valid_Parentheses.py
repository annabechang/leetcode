'''
20. Valid Parentheses
Easy

2634

131

Favorite

Share
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {"(":")", "[":']', '{':'}'}
        
        for parentheses in s:
            if parentheses in lookup:  
                stack.append(parentheses)
                #stored found ( in stack
                # if the ( match with )
            elif len(stack) == 0 or lookup[stack.pop()] != parentheses:
                #use pop to pop the (, put it into lookup see if it matches 
                return False
                #len(stack) == 0 : for situation where it's input with ) 
                
        return len(stack) == 0
        
        
"""
Success
Details 
Runtime: 52 ms, faster than 24.18% of Python3 online submissions for Valid Parentheses.
Memory Usage: 13.3 MB, less than 5.22% of Python3 online submissions for Valid Parentheses.
"""
