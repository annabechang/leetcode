"""
342. Power of Four
Easy

419

183

Add to List

Share
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?
"""
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        
        if num == 1:
            return True
        elif num <=2:
            return False
        while num>4:
            if num%4 == 0:
                num/=4
            else:
                return False 
        if num == 4:
            return True
        else:
            return False 
"""
Runtime: 28 ms, faster than 74.65% of Python3 online submissions for Power of Four.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Power of Four.
"""
# intiger has a range, less than 2147483648
# store all the power of 4 into a dict 

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        
        nums = [1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576, 4194304, 16777216, 67108864, 268435456, 1073741824]
        return num in nums
"""
Success
Details 
Runtime: 32 ms, faster than 42.48% of Python3 online submissions for Power of Four.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Power of Four.
"""
"""
# using bit 
# first check if it's a power of 2 
any 2^n -1 = 111...b
2 = 2^1.  2-1 = 1 (1b)
4 = 2^2.  4-1 = 3 (11b)
8 = 2^3.  8-1 = 7 (111b)
Example with 8: 0100 & (0100 - 1) --> (0100 & 0011) --> 0000
Example with 3: 0011 & (0011 - 1) --> (0011 & 0010) --> 0010
Example with 13: 1101 & (1101 - 1) --> (1101 & 1100) --> 1100

#check if it's power of 4
each hexadecimal can be rewrote as a 4 digital binary. 
0x means hexadecimal, 5 is 4+1 = 2^2 +2^0. So 5 is 0101. 0x555 = 0101 0101 0101.
11 10 9 8 |7 6 5 4 | 3 2 1 0
 0  1 0 1 |0 1 0 1 | 0 1 0 1
        5 |      5 |     5 |
Therefore, to extract bits set at index, 0, 2, 4, 6, 8 .... 
one need to use the above mask of 0x55555555. Remember each 5 represents 4 bit.
The appearance of 0x55555555 may seem rather random, 
but recall that its binary representation alternates between zeroes and ones: 0101010101…. 
The bitwise AND of num with this number gives a version of num where 
every other bit (the 2's bit, the 8's bit, the 32's bit) has been removed 
and the remaining bits (1's, 4's, 16's, …) are kept.
num	        01110010 =114 = 64+32+16+2
0x55        01010101 =85  = 64+16+4+1
num & 0x55	01010000 = 80 = 64+16

num            0000000000010000 = 16
0x55555555     0101010101010101 
numx0x55555555 0000000000010000 = 16  

a number if it is power of 4 after and 0x55555555 it would still be itself
"""
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        
        return num > 0 and (num&(num-1)) == 0 and (num & 0x55555555)==num
"""
Success
Details 
Runtime: 24 ms, faster than 92.94% of Python3 online submissions for Power of Four.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Power of Four.
"""
