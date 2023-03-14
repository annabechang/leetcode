"""

Given two integers a and b, return the sum of the two integers without using the operators + and -.

import numpy as np
class Solution:

    def getSum(self, a: int, b: int) -> int:

        # bitshortner = 0xffffffff

        # while (b & bitshortner)>0:
        #     carry = (a & b )<<1
        #     a = (a^b)
        #     b = carry
        # return (a & bitshortner) if b > 0 else a
        while b!= 0:
            a,b = np.int32(a ^ b), np.int32((a & b)<<1)
            print(a,b)
        return int(a)
"""
