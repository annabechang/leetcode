"""
303. Range Sum Query - Immutable
Easy

683

924

Add to List

Share
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:

Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:

You may assume that the array does not change.
There are many calls to sumRange function.

the idea is to sum to the j and then minus the sum to before i
for example
sumRange(2, 5) -> -1
sum ~ 5 = -3
sum ~ 1 = -2
-3 - (-2) = -1

"""



class NumArray:

    def __init__(self, nums: List[int]):
        self.accu = [0] #initial array. accu = accurate. accu record the sum before num  
        for num in nums:
            self.accu.append(self.accu[-1]+num)
        #print (self.accu)
    
    def sumRange(self, i: int, j: int) -> int:
        return self.accu[j+1] - self.accu[i] #

        
        
#You may assume that the array does not change.         

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
"""
Success
Details 
Runtime: 80 ms, faster than 69.47% of Python3 online submissions for Range Sum Query - Immutable.
Memory Usage: 16.3 MB, less than 100.00% of Python3 online submissions for Range Sum Query - Immutable.

"""

class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.sums = [0]*(n+1)
        for i in range(1,n+1):
            self.sums[i] = self.sums[i-1]+nums[i-1]
    
    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j+1] - self.sums[i]

        
        
#You may assume that the array does not change.         

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
