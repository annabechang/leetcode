"""
121. Best Time to Buy and Sell Stock
Easy

2539

120

Favorite

Share
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0

        max_profit, min_price = 0,float('inf')

        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)

        return max_profit
"""
Success
Details 
Runtime: 44 ms, faster than 78.99% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 13.8 MB, less than 75.34% of Python3 online submissions for Best Time to Buy and Sell Stock.

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lenth = len(prices)
       
        if lenth <= 1:
            return 0

        max_price = prices[lenth-1]
        max_profit = 0
        
        for i in range(lenth-1, -1, -1):
            max_price = max(max_price, prices[i]) 
            difference = max_price - prices[i]
            max_profit = max(max_profit, difference)
 
        return max_profit
"""
Success
Details 
Runtime: 48 ms, faster than 50.42% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 14 MB, less than 49.23% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lenth = len(prices)
       
        if lenth <= 1:
            return 0

        max_price = prices[lenth-1]
        max_profit = 0
        
        for i in range(lenth-1, -1, -1):
            max_price = max(max_price, prices[i]) 
            
            if max_price - prices[i] > max_profit:
                max_profit = max_price - prices[i]
 
        return max_profit
        
"""
Success
Details 
Runtime: 36 ms, faster than 99.24% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 13.8 MB, less than 75.84% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        minPro, maxPro = prices[0], 0
        
        for i in range(1, len(prices)):
            minPro = min(minPro, prices[i])
            maxPro = max(maxPro, prices[i]-minPro)
        return maxPro
"""
Success
Details 
Runtime: 44 ms, faster than 78.99% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 14 MB, less than 44.59% of Python3 online submissions for Best Time to Buy and Sell Stock.

"""


# option 2
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        # max = prices[0]
        pro = 0
        

        for i in range(len(prices)):
            # print(i,prices[i])
            if prices[i]<min:
                # print("if1")
                min = prices[i]
                
                # for j in range(0,i):
                    
                #     if prices[j]<min:
                #         min = prices[j]
            elif prices[i] - min > pro:
                pro = prices[i] - min 
            
        
        
        return pro
