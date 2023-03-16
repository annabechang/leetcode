class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # dp = [False]*len(nums)
        goal = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            
            if i+nums[i] >=goal:
                goal = i
        # goal = 0 or non 0
        return True if goal == 0 else False
