"""
4. Median of Two Sorted Arrays

Hard

4503

629

Favorite

Share
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""
"""
Our array looks like this:
        left        right
A: [0, ... , i-1] [i, ... m-1]
B: [0, ... , j-1] [j, ... n-1]

if we can ensure:
1. len(left part) = len(right part)
2. max(left_part) <= min(right part)
3. n >= m (make sure j is a non negative since 0<= i <= m, j = (m+n)/2 -i, if n<m and i ≒ m, j could be negative)

=> then 
median = [max(left part)+min(right part)] / 2 

to find the i and j that satisfied this condition:
1. i + j = m - i + n - j 
   if i ≒ m:
   => m + j = m - m + n - j
   => j = (m+n)/2 -i
   
2. B[j-1] <= A[i] and A[i-1] <= B[j]




"""
class Solution(object):
    def findMedianSortedArrays(self, A, B):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
    
        m,n = len(A), len(B)
        
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError
        
        imin, imax, half_len = 0, m, (m+n+1)//2
        
        while imin <= imax:
            i = (imin+imax) // 2
            j = half_len - i
            
            if i < m and B[j-1] > A[i]:
                imin = i + 1
            #elif j < n and A[i-1] > B[j]:
            elif i > 0 and A[i-1] > B[j]:
                imax = i -1 
            else:
                if i == 0:
                    max_of_left = B[j-1]
                elif j == 0:
                    max_of_left = A[i-1]
                else:
                    max_of_left = max(A[i-1], B[j-1])
                    
                if (m+n) %2 == 1:
                    return max_of_left
                if i == m:
                    min_of_right = B[j]
                elif j == n :
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])
                return (max_of_left+min_of_right)/ 2.0

"""
Success
Details 
Runtime: 68 ms, faster than 97.03% of Python online submissions for Median of Two Sorted Arrays.
Memory Usage: 12 MB, less than 16.14% of Python online submissions for Median of Two Sorted Arrays.


"""
