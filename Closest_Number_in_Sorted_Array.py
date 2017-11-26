"""
Lintcode 459

Given a target number and an integer array A sorted in ascending order, 
find the index i in A such that A[i] is closest to the given target.

Return -1 if there is no element in the array.

Notice
There can be duplicate elements in the array, and we can return any of the indices with same value.

Example
Given [1, 2, 3] and target = 2, return 1.
Given [1, 4, 6] and target = 3, return 1.
Given [1, 4, 6] and target = 5, return 1 or 2.
Given [1, 3, 3, 4] and target = 2, return 0 or 1 or 2.

Binary Search
O(logN) time complexity
"""
class Solution:
    def closestNumber(self, nums, target):
        if not nums or len(nums) == 0:
            return -1
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid
        if abs(nums[start] - target) <= abs(nums[end] - target):
            return start
        else:
            return end
