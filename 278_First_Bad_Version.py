"""
278. First Bad Version
Easy

825

483

Favorite

Share
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 
"""
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        r = n-1
        l = 0
        while r>=l:
            mid = (r+l)//2
            if isBadVersion(mid) == False:
                l = mid+1 
            else:
                r = mid-1
        return l

"""
Success
Details 
Runtime: 24 ms, faster than 99.05% of Python3 online submissions for First Bad Version.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for First Bad Version.
"""
