"""
38. Count and Say
Easy

700

5295

Favorite

Share
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11 -> the previous "1" is read as "one 1" -> "11"
3.     21 -> the previous "11" is read as "two 1" -> "21"
4.     1211 -> the previous is "21" is read as "one 2 one 1" -> 1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

 

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        seq = '1'
        for i in range(n-1):
            seq = self.getNext(seq)
        return seq 
    
    def getNext(self, seq):
        i, next_seq = 0, ""
        while i <len(seq):
            count = 1 #initial
        #i < len(seq) "-1" or it would be out of range at the last position
        #seq[i] == seq[i+1] : if it's 11 
            while i < len(seq) -1 and seq[i] == seq[i+1]:
                count +=1
                i +=1
            #seq[i] != seq[i+1]: 12 
            next_seq += str(count) + seq[i]
            i += 1
        return next_seq
"""
Success
Details 
Runtime: 40 ms, faster than 79.13% of Python3 online submissions for Count and Say.
Memory Usage: 13 MB, less than 5.11% of Python3 online submissions for Count and Say.
"""






