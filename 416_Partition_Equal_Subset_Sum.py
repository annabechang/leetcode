"""
416. Partition Equal Subset Sum

Medium

1261

36

Favorite

Share
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.
 

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
 

Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
"""

"""
using dynamic programing
"""
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numSum = sum(nums)
        
        if numSum % 2 != 0:
            return False
        
        dp = [0] * (numSum +1)
        dp[0] = 1
        
        for num in nums:
            for i in range(numSum , -1, -1):
                if dp[i]:   #last iteration dp[i] is true-> dp[num+i] = true
                    dp[num+i] = 1
            if dp[int(numSum/2)] == 1:
                return True
        return False
"""
Success
Details 
Runtime: 496 ms, faster than 62.19% of Python online submissions for Partition Equal Subset Sum.
Memory Usage: 11.8 MB, less than 84.46% of Python online submissions for Partition Equal Subset Sum.

"""
