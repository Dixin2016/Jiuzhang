"""
An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. 
The black pixels are connected, i.e., there is only one black region. 
Pixels are connected horizontally and vertically. 
Given the location (x, y) of one of the black pixels, 
return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

https://discuss.leetcode.com/topic/29086/clear-binary-search-python
https://www.jiuzhang.com/solutions/smallest-rectangle-enclosing-black-pixels
"""
class Solution(object):
    # @param image {List[List[str]]}  a binary matrix with '0' and '1'
    # @param x, y {int} the location of one of the black pixels
    # @return an integer
    def minArea(self, image, x, y):
        # Write your code here
        n, m = len(image), len(image[0])
        if m == 0 or n == 0 or not image:
            return False

        left = self.findLeft(image, 0, y)
        right = self.findRight(image, y, m - 1)
        top = self.findTop(image, 0, x)
        bottom = self.findBottom(image, x, n - 1)

        return (right - left + 1) * (bottom - top + 1)

    def findLeft(self, image, start, end):
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.isEmptyCol(image, mid):
                start = mid
            else:
                end = mid
        if self.isEmptyCol(image, start):
            return end
        return start

    def findRight(self, image, start, end):
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.isEmptyCol(image, mid):
                end = mid
            else:
                start = mid
        if self.isEmptyCol(image, end):
            return start
        return end

    def findTop(self, image, start, end):
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.isEmptyRow(image, mid):
                start = mid
            else:
                end = mid
        if self.isEmptyRow(image, start):
            return end
        return start

    def findBottom(self, image, start, end):
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.isEmptyRow(image, mid):
                end = mid
            else:
                start = mid
        if self.isEmptyRow(image, end):
            return start
        return end

    def isEmptyCol(self, image, col):
        for i in range(len(image)):
            if image[i][col] == '1':
                return False
        return True

    def isEmptyRow(self, image, row):
        for i in range(len(image[0])):
            if image[row][i] == '1':
                return False
        return True
      
   """
   Be careful about the test case and line 74 and 80.
   If test cases are like below which contains integer 0s and 1s, then line 74 and 80 should be == 1;
   if test cases contain string '0's and '1's, line 74 an 80 should be == '1'
   B = [[0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,1,0,0,0],
     [0,0,1,1,1,1,1,1,0,0],
     [0,0,0,0,0,0,1,0,0,0],
     [0,0,0,0,0,0,0,0,0,0]]
   """
