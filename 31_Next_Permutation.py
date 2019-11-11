"""
31. Next Permutation
Medium

2360

784

Favorite

Share
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums: return None
        n = len(nums)
        i = n -1
        j = -1
        
        while i > 0:
            if nums[i] > nums[i-1]: # first one violates the trend
                j=i-1
                break
            i-=1
            
        for i in range(n-1, -1,-1):
            if nums[j] < nums[i]:
                nums[i],nums[j]=nums[j],nums[i] # swap position
                nums[j+1:] = sorted(nums[j+1:]) # sort rest
                return 



"""
Success
Details 
Runtime: 36 ms, faster than 99.33% of Python3 online submissions for Next Permutation.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Next Permutation.
"""
