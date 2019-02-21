"""
9. Palindrome Number


Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up:

Coud you solve it without converting the integer to a string?

"""

class Solution:
    def isPalindrome(self, x: 'int') -> 'bool':
        rev = int(str(abs(x))[::-1])
        return True if x == rev else False
    
    #    if x == rev:
     #       return True
      #  else:
       #     return False
       
"""
Success
Details 
Runtime: 224 ms, faster than 99.84% of Python3 online submissions for Palindrome Number.
Memory Usage: 12.7 MB, less than 83.57% of Python3 online submissions for Palindrome Number.
"""


#solution without converting x to str

class Solution:
    def isPalindrome(self, x: 'int') -> 'bool':
        num = 0
        a = abs(x)
        
        while (a != 0):
            temp = a % 10
            # knowing what's the num on the rightest
            num = num*10 +temp
            # make the previous num move to the left 
            a = int(a /10)
            # remove the alrady added number 
        if x >= 0 and x == num:
            return True
        else:
            return False


"""
Success
Details 
Runtime: 256 ms, faster than 72.35% of Python3 online submissions for Palindrome Number.
Memory Usage: 12.7 MB, less than 86.27% of Python3 online submissions for Palindrome Number.
"""



