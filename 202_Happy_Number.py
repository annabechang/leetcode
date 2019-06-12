"""
202. Happy Number

Easy

868

222

Favorite

Share
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

"""
"""
Floyd Cycle Detection Algorithm
non-happy number: 200 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4 ->... ->4
                  slow
                  fast 
when it's a non happy number, it will eventually come to a cycle -> cycled linked list 
"""
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow, fast = n,n

        while True:
            slow = self.digitSquareSum(slow)
            fast = self.digitSquareSum(fast)
            fast = self.digitSquareSum(fast)
            if slow == fast:
                break 
        return slow == 1

    def digitSquareSum(self,n):
        sum = 0
        while n>0:
            temp = n % 10
            sum += temp**2
            n /= 10
        return sum
 """
Details 
Runtime: 24 ms, faster than 78.60% of Python online submissions for Happy Number.
Memory Usage: 11.7 MB, less than 70.76% of Python online submissions for Happy Number.
 """
"""
Use dictionary to store the preivous values.
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num_dict = {}
        
        while n != 1:
            if n in num_dict:
                return False
            else:
                num_dict[n] = True         
                n = sum([int(i) ** 2 for i in str(n)])
          
        return True
 """
 Success
Details 
Runtime: 12 ms, faster than 99.11% of Python online submissions for Happy Number.
Memory Usage: 11.9 MB, less than 10.89% of Python online submissions for Happy Number.
 """
