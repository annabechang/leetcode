"""
22. Generate Parentheses
Medium

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        
        result = []
        self.helper(n,n,'', result)
        return result 
    
    def helper(self, l, r, item, result):
        #remove not good ne
        #if num of l( > ) or num ) > (
        if r < l:
            return
        
        if l == 0 and r == 0:
            result.append(item)
        if l > 0:
            self.helper(l-1, r, item+'(', result)
        if r > 0:
            self.helper(l, r-1, item+')', result)
        
"""
Success
Details 
Runtime: 32 ms, faster than 98.99% of Python3 online submissions for Generate Parentheses.
Memory Usage: 14.1 MB, less than 6.67% of Python3 online submissions for Generate Parentheses.
"""
