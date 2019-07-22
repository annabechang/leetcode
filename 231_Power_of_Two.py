"""
231. Power of Two
Easy

467

128

Favorite

Share
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false
"""
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n % 2 == 0 and n >= 1:
            n /= 2
        return True if n == 1 else False
"""
Success
Details 
Runtime: 32 ms, faster than 92.94% of Python3 online submissions for Power of Two.
Memory Usage: 14 MB, less than 5.80% of Python3 online submissions for Power of Two.

"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n-1)) == 0 
        
"""
Success
Details 
Runtime: 44 ms, faster than 15.10% of Python3 online submissions for Power of Two.
Memory Usage: 14 MB, less than 5.80% of Python3 online submissions for Power of Two.

"""
"""
It's figuring out if n is either 0 or an exact power of two.

It works because a binary power of two is of the form 1000...000 and subtracting one will give you 111...111. Then, when you AND those together, you get zero, such as with:

  1000 0000 0000 0000
&  111 1111 1111 1111
  ==== ==== ==== ====
= 0000 0000 0000 0000
Any non-power-of-two input value (other than zero) will not give you zero when you perform that operation.

For example, let's try all the 4-bit combinations:

     <----- binary ---->
 n      n    n-1   n&(n-1)
--   ----   ----   -------
 0   0000   0111    0000 *
 1   0001   0000    0000 *
 2   0010   0001    0000 *
 3   0011   0010    0010
 4   0100   0011    0000 *
 5   0101   0100    0100
 6   0110   0101    0100
 ~ credit to @paxdiablo
"""
