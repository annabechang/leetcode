"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0     0= 0
1 --> 1     1= 1+dp[n-1]
2 --> 10    1= 1+dp[n-2]
3 --> 11    2= 1+dp[n-2]
4 --> 100   1= 1+dp[n-4]
5 --> 101   2= 1+dp[n-4]


6 --> 110   2= 1+dp[n-4]
7 --> 111   3=1+dp[n-4]
8 --> 1000   1 = 1+dp[n-8]

找出那個dp的規律之後就是寫一個簡單的公式
"""

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        
        offset = 1

        for i in range(1,n+1):
            
            if offset *2 == i:
                offset = i
            dp[i] = 1+dp[i-offset]
            print(i, dp[i],offset)
        return dp    
