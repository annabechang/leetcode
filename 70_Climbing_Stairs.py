"""
70. Climbing Stairs
Easy

2013

75

Favorite

Share
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        # n = 1: 1
        # n = 2: 2
        # n = 3: 3
        # n = 4: 4
        # n = 5: 8
        # ... fibonacci

        prev, current = 0,1
        for i in range(n):
            prev, current = current, prev+current 
        return current

"""
Success
Details 
Runtime: 36 ms, faster than 76.06% of Python3 online submissions for Climbing Stairs.
Memory Usage: 13.2 MB, less than 5.18% of Python3 online submissions for Climbing Stairs.

"""

"""
class Solution:
    def climbStairs(self, n: int) -> int:

        one, two = 1,1

        for i in range(n-1):
            tmp = one
            one = one+two
            two = tmp
            
        return one

"""


