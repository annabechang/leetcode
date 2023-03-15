"""
191. Number of 1 Bits

Easy

430

380

Favorite

Share
Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).

 

Example 1:

Input: 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
Example 2:

Input: 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
Example 3:

Input: 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
 

Note:

Note that in some languages such as Java, there is no unsigned integer type. In this case, the input will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3 above the input represents the signed integer -3.
 

Follow up:

If this function is called many times, how would you optimize it?
"""
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        
        while n:
            res += n & 1
            n >>= 1
        return res

"""
Success
Details 
Runtime: 16 ms, faster than 94.11% of Python online submissions for Number of 1 Bits.
Memory Usage: 11.7 MB, less than 74.71% of Python online submissions for Number of 1 Bits.
"""
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        
        while n:
            n &= n-1
            res += 1
        return res
"""
Think of a number in binary 
n = 1001, n - 1 is 1000. n & (n - 1) = 1000. count+=1  will just cancel the last 1.
n = 1000, n - 1 is 0111. n & (n - 1) = 000 done
Success
Details 
Runtime: 16 ms, faster than 94.11% of Python online submissions for Number of 1 Bits.
Memory Usage: 11.8 MB, less than 24.36% of Python online submissions for Number of 1 Bits.
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        count =0
        while n > 0:
            count += n % 2 
            n = n>>1
        
        return count  
