"""
LintCode 462 - Total Occurrence of Target

Given a target number and an integer array sorted in ascending order. 
Find the total number of occurrences of target in the array.

Example 
Given [1, 3, 3, 4, 5] and target = 3, return 2.
Given [2, 2, 3, 4, 6] and target = 4, return 1.
Given [1, 2, 3, 4, 5] and target = 6, return 0.

Time complexity in O(logn)

Binary Search
"""

class Solution(object):
        def totalOccurrence(self, nums, target):
        if not nums or len(nums) == 0:
            return False
        if target < nums[0] or target > nums[-1]:
            return 0

        # The first occurrance of target
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid
        if nums[start] == target:
            left = start
        elif nums[end] == target:
            left = end
        else:
            return 0

        # The last occurrance of target
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] <= target:
                start = mid
            else:
                end = mid
        if nums[end] == target:
            right = end
        elif nums[start] == target:
            right = start

        return right - left + 1
