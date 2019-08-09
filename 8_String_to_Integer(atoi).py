"""
8. String to Integer (atoi)
Medium

1035

6470

Favorite

Share
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.
"""
class Solution:
    def myAtoi(self, str: str) -> int:
        #get ride of the white space using strip
        #strip function default is white space
        stripS = str.strip()
        # now we have a string without white space
        
        # is it empty?
        if stripS == "" or stripS == "-" or stripS == "+":
            return 0
        
        # is there something we can't convert in front
        # like example 4
        # match(patter, where to search->string without +-)
        # lstrip: get ride of the things on the left
        # s1 = search 1 
        s1 = re.match('[^\d]+',(stripS.lstrip("-")).lstrip("+"))

        if s1 != None:
            return 0
        
        else: 
            #does it have a digit with or without +-
            # use group to return the found value
            s1 = re.search('\-*\+*\d+', stripS).group()
            
        # what if it's ++42 -+42 --42
        # we did not include +-42 because 
        # we first get ride of + -> -42 -> s1 != none
        # -> return 0
        if s1[0:2] == "--" or s1[0:2] == "-+" or s1[0:2] == "++":
            return 0
        
        #now we chcek if it's out of range
        
        result = int(s1)
        if result > 0:
            return 2147483648 if result > 2147483648 else result
        else: 
            return -2147483648 if result < -2147483648 else result
        
        
"""
Success
Details 
Runtime: 36 ms, faster than 92.49% of Python3 online submissions for String to Integer (atoi).
Memory Usage: 13.8 MB, less than 5.95% of Python3 online submissions for String to Integer (atoi).
"""
