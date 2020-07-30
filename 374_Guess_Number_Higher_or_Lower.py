"""
374. Guess Number Higher or Lower
Easy

420

1755

Add to List

Share
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example :

Input: n = 10, pick = 6
Output: 6
"""
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n
        while l <= r:
            m = (l+r)//2
            if guess(m) == -1:
                r = m -1
            elif guess(m) == 0:
                return m
            else:
                l = m + 1    

"""
Success
Details 
Runtime: 48 ms, faster than 14.95% of Python3 online submissions for Guess Number Higher or Lower.
Memory Usage: 13.9 MB, less than 22.30% of Python3 online submissions for Guess Number Higher or Lower.
"""
