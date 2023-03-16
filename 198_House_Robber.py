"""
198. House Robber

Easy

2513

76

Favorite

Share
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.

"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0 
        
        for num in nums:
            last, now = now, max(now, last + num)
        return now
"""
Details 
Runtime: 24 ms, faster than 37.06% of Python online submissions for House Robber.
Memory Usage: 11.8 MB, less than 46.91% of Python online submissions for House Robber.
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
#         rob1, rob2 = 0,0
# # rob1, rob2, n, n+1
#         for n in nums: 
#             temp = max(n+rob1, rob2)
#             # decite to rub n or not
#             rob1 = rob2
#             # move one hop to n+1
#             rob2 = temp 
#         return rob2 
        dp = [0]*len(nums)
        dp[0] = nums[0]
        if len(nums)>1:
            dp[1] = max(nums[0],nums[1])
            for i in range(2, len(nums)):
                dp[i]= max(dp[i-1], nums[i]+dp[i-2])
        return dp[-1]
