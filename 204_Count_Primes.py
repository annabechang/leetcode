"""
204. Count Primes
Easy

1088

413

Favorite

Share
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

"""
#sieve of Eratosthenes

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1 :
            return 0
        
        nums = [True] * n
        nums[0] = False
        nums[1] = False
        
        for i in range(n):
            if nums[i] == True:
                for j in range(i+i, n, i):
                # i+i = 2*i to n. with the gape equal to i 
                # if it can be devided by i then mark it false
                    nums[j] = False
                    
        return sum(nums)

"""
Success
Details 
Runtime: 724 ms, faster than 42.23% of Python3 online submissions for Count Primes.
Memory Usage: 24.7 MB, less than 86.40% of Python3 online submissions for Count Primes.

"""
