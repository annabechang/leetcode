"""
17. Letter Combinations of a Phone Number
Medium
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
"""
#create a digit map dictionary
#roun1: read"2"
#      possible output : tmp = ["a","b","c"]
#      result = tmp
#round2: read"3"
#       possible fetch : ch = ["d","e","f"]
#round3:
#       result+fetch = output
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        
        digit_map = {
            0:"0",
            1:"1",
            2:"abc",
            3:"def",
            4:"ghi",
            5:"jkl",
            6:"mno",
            7:"pqrs",
            8:"tuv",
            9:"wxyz"
        }
        
        result = [""]
        
        for digit in digits:
            tmp = []
            for ch in digit_map[int(digit)]:
                for str in result:
                    tmp.append(str + ch)
            result = tmp
        return result 
"""
Success
Details 
Runtime: 32 ms, faster than 92.66% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 13.7 MB, less than 5.88% of Python3 online submissions for Letter Combinations of a Phone Number.

"""
