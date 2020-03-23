"""
344. Reverse String
Easy

1145

640

Add to List

Share
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

 

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        m = len(s)//2
        
        for i in range(m):
            s[i], s[-i-1] = s[-i-1], s[i]
            # index = 0,1,2,3
            # i = 0: 0 -> 3 = -i-1 = -0-1=-1
            # i = 1: 1 -> 2 = -i-1 = -1-1=-2 
"""
Success
Details 
Runtime: 220 ms, faster than 38.11% of Python3 online submissions for Reverse String.
Memory Usage: 17.4 MB, less than 94.19% of Python3 online submissions for Reverse String.
"""
