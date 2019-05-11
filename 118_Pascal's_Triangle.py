"""
118. Pascal's Triangle
Easy

682

78

Favorite

Share
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        #first make the [] for # of numRows
        for i in range(runRows):
            result.append([])
            
            # every row we have i element. but i started from 0, so +1
            for j in range(i+1):
               if j in (0,i):
                    result[i].append(1)
            
                else:
                    result[i].append(result[i-1][j-1]+result[i-1][j])
                    
        return result                

"""
Success
Details 
Runtime: 32 ms, faster than 99.14% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 13.2 MB, less than 5.83% of Python3 online submissions for Pascal's Triangle.
Success
Details 
Runtime: 32 ms, faster than 99.14% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 13.2 MB, less than 5.83% of Python3 online submissions for Pascal's Triangle.
"""
