"""
Link:
http://www.lintcode.com/en/problem/find-peak-element-ii/

Question:
There is an integer matrix which has the following features:

The numbers in adjacent positions are different.
The matrix has n rows and m columns.
For all i < m, A[0][i] < A[1][i] && A[n - 2][i] > A[n - 1][i].
For all j < n, A[j][0] < A[j][1] && A[j][m - 2] > A[j][m - 1].
We define a position P is a peek if:

A[j][i] > A[j+1][i] && A[j][i] > A[j-1][i] && A[j][i] > A[j][i+1] && A[j][i] > A[j][i-1]

Find a peak element in this matrix. Return the index of the peak.

Example:
Given a matrix:

[ [1 ,2 ,3 ,6 ,5], 
  [16,41,23,22,6], 
  [15,17,24,21,7], 
  [14,18,19,20,10], 
  [13,14,11,10,9] ]

return index of 41 (which is [1,1]) or index of 24 (which is [2,2])

Thoughts

从中间行，找到这一行的最大数
如果上面数比它大，则上半部必然有一个Peak，对下面也是
二分法

"""

class Solution:
    #@param A: An list of list integer 
    #@return: The index of position is a list of integer, for example [2,2]
    def findPeakII(self, A):
        # write your code here
        
        if not A or len(A) == 0 or len(A[0]) == 0:
            return []

        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            col = self.findmaxcol(A[mid])
            if A[mid][col] < A[mid - 1][col]:
                end = mid
            elif A[mid][col] < A[mid + 1][col]:
                start = mid
            else:
                return [mid, col]
        if A[start][col] > A[end][col]:
            return [start, col]
        else:
            return [end, col]

        return []

    def findmaxcol(self, list):
        ans = 0
        for i in range(len(list)):
            if list[ans] < list[i]:
                ans = i
        return ans
