"""
190. Reverse Bits
Easy

558

174

Favorite

Share
Reverse bits of a given 32 bits unsigned integer.

 

Example 1:

Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
Example 2:

Input: 11111111111111111111111111111101
Output: 10111111111111111111111111111111
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10101111110010110010011101101001.
 

Note:

Note that in some languages such as Java, there is no unsigned integer type. In this case, both input and output will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above the input represents the signed integer -3 and the output represents the signed integer -1073741825.
 

Follow up:

If this function is called many times, how would you optimize it?
"""
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bit = '{:032b}'.format(n)
        reverse_bit = bit[::-1]
        return int(reverse_bit, 2)
"""
Success
Details 
Runtime: 8 ms, faster than 99.80% of Python online submissions for Reverse Bits.
Memory Usage: 11.8 MB, less than 22.81% of Python online submissions for Reverse Bits.
"""


"""
Divide and Conquer
swap two bits, 4 bits, 8 bits, 16 bits and 32 bits, Then it reversed
For example, if there are 8 bit binary number abcdefgh,
    the process is as follow:
    abcdefgh -> efghabcd -> ghefcdab -> hgfedcba
0x: 16 bits into binary it represend as follow:
0xaaaaaaaa = 10101010101010101010101010101010 (even 1, odd 0）

0x55555555 = 1010101010101010101010101010101 (even 0, odd 1）

0x33333333 = 110011001100110011001100110011 (1,0 appears every two numbers)

0xcccccccc = 11001100110011001100110011001100 (0,1 appears every two numbers)

0x0f0f0f0f = 00001111000011110000111100001111 (1,0 appears every four numbers)

0xf0f0f0f0 = 11110000111100001111000011110000 (0,1 appears every four numbers)
"""
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n = ((n >> 16 ) | (n << 16))
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n
"""
for example:
n= ABCD. ABCD each represent a 8 bit number
second line: n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
0xff00ff00: ABCD -> A0C0, then >>8 shift 8 bits to the right -> 0A0C
0x00ff00ff: ABCD -> 0B0C, then <<8 shift 8 bits to the left -> B0C0
combine both -> BACD
"""
"""
Success
Details 
Runtime: 8 ms, faster than 99.80% of Python online submissions for Reverse Bits.
Memory Usage: 11.8 MB, less than 37.15% of Python online submissions for Reverse Bits.
"""
