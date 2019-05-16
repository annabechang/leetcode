"""
119. Pascal's Triangle II
Easy

462

164

Favorite

Share
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?


"""
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1] + [0]*rowIndex
        
        for i in range(rowIndex):
            result[0] = 1
            for j in range(i+1,0,-1):
                result[j] += result[j-1]
                
        return result 
"""
Success
Details 
Runtime: 36 ms, faster than 85.58% of Python3 online submissions for Pascal's Triangle II.
Memory Usage: 13.1 MB, less than 66.21% of Python3 online submissions for Pascal's Triangle II.

"""
