"""
6. ZigZag Conversion
Medium
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""
"""
first work through to see the pattern and get a better understanding:
s = "PAYPALISHIRING" numRows = 3
iteration 1 "P", row [0] 
iteration 2 "A", row [1] +1
iteration 3 "Y", row [2] +1
iteration 4 "P", row [1] -1
iteration 5 "A", row [0] -1
iteration 6 "L", row [1] +1
iteration 7 "I", row [2] +1
...
--> row == 0 : step = 1
    row == numRows -1 (hit the end row): step -1
    row = row + step 
"""
"""
EX: s = "PAY"
when numRows == 1 : return s : "PAY"
when numRows >=1 lem(s): return s: 
"P
 A
 Y" 
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
            
        # create a list of empty strings 
        zigzag = ['' for x in range(numRows)]
        
        # initialize the sequence. row = row index  
        row, step = 0 , 1
        
        ## add s[character] to the list using row index## 
        for char in s:
            # add character to it's row in zigzag 
            zigzag[row] += char 
            
            if row == 0:
                step = 1
            elif row == numRows -1:
                step = -1
            
            row += step
            
        #join the list together. this enable us to return the result the way we want
        return ''.join(zigzag)
"""
Success
Details 
Runtime: 52 ms, faster than 98.32% of Python3 online submissions for ZigZag Conversion.
Memory Usage: 13.8 MB, less than 9.13% of Python3 online submissions for ZigZag Conversion.
"""
