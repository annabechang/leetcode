"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
initialize 一個array 是amount +1, amount+1 長。然後for loop through 那個array 跟coin. 如果要換的amount>= coin 就是result[i] vs result[i-面額]+1 
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # coins.sort()
        res = [amount+1]*(amount+1)
        res[0] = 0
        for i in range(amount+1):
            for coin in coins:
                if i >= coin:
                    res[i] = min(res[i],res[i-coin]+1)
        if res[amount] == amount+1:
            return -1
        return res[amount]