"""
263. Ugly Number
Easy

268

487

Favorite

Share
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example 1:

Input: 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: 8
Output: true
Explanation: 8 = 2 × 2 × 2
Example 3:

Input: 14
Output: false 
Explanation: 14 is not ugly since it includes another prime factor 7.
Note:

1 is typically treated as an ugly number.
Input is within the 32-bit signed integer range: [−231,  231 − 1].
"""
class Solution:
    def isUgly(self, num: int) -> bool:
        for prime in 2,3,5:
            while num % prime == 0 < num :
                num /= prime
        return num == 1

"""
Success
Details 
Runtime: 40 ms, faster than 55.74% of Python3 online submissions for Ugly Number.
Memory Usage: 14 MB, less than 6.67% of Python3 online submissions for Ugly Number.

"""
class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        
        primes = [2,3,5]
        for prime in primes:
            while num % prime == 0 < num :
                num /= prime
            if num == 1:
                return True
        return False

"""
Success
Details 
Runtime: 40 ms, faster than 55.74% of Python3 online submissions for Ugly Number.
Memory Usage: 13.9 MB, less than 6.67% of Python3 online submissions for Ugly Number.

"""
