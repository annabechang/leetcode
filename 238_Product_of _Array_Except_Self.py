"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 """
 
 class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        
        # store previc in ans
        n = len(nums)
        ans = [1]*n
        for i in range(1,n):
            ans[i] = ans[i-1]*nums[i-1]
        #     # print(i, ans)
        # print(ans)
        # this is pre
        # ans times the post fix is the final ans
        pos = 1
        ans = ans[::-1]
        for i in range(1,n):
            pos = pos*nums[-i]
            # print(pos)
            ans[i] = ans[i]*pos
        # for i in range()
        ans = ans[::-1]
        print(ans)
        return ans
