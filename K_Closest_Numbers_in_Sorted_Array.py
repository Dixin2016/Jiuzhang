"""
LintCode 460. K Closest Numbers In Sorted Array

Given a target number, a non-negative integer k and an integer array A sorted in ascending order,
find the k closest numbers to target in A, sorted in ascending order by the difference between the number and target.
Otherwise, sorted in ascending order by number if the difference is same.

Example
Given A = [1, 2, 3], target = 2 and k = 3, return [2, 1, 3].
Given A = [1, 4, 6, 8], target = 3 and k = 3, return [4, 1, 6].

Challenge 
O(logn + k) time complexity
"""
class Solution:
    def kClosestNumbers(self, nums, target, k):
        if not nums or len(nums) == 0 or k == 0:
            return []
        
        if target <= nums[0]:
            return nums[0 : k]
        if target >= nums[-1]:
            return nums[-k:]
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid
        
        res = []
        while k > 0 and (start >= 0 or end < len(nums)):
            if (start >=0 and end < len(nums) and abs(nums[start] - target) <= abs(nums[end] - target)) or end >= len(nums):
                res.append(nums[start])
                start -= 1
            elif (start >=0 and end < len(nums) and abs(nums[start] - target) > abs(nums[end] - target)) or start < 0:
                res.append(nums[end])
                end += 1
            k -= 1
        return res
