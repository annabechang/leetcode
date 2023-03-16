"""
basically just write the house robber one into a function and call it twice. 
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        def robber(nums):
            dp = [0]*len(nums)
            dp[0] = nums[0] 
            
            dp[1] = max(nums[0],nums[1])
            for i in range(2, len(nums)):
                dp[i]= max(dp[i-1], nums[i]+dp[i-2])
            return dp[-1]

        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums)
        return max(robber(nums[:-1]), robber(nums[1:]))
