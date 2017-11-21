"""
Lintcode 39. Recover Rotated Sorted Array 

Given a rotated sorted array, recover it to sorted array in-place.

What is rotated array?

For example, the orginal array is [1,2,3,4], The rotated array of it can be [1,2,3,4], [2,3,4,1], [3,4,1,2], [4,1,2,3]
Example
[4, 5, 1, 2, 3] -> [1, 2, 3, 4, 5]

Challenge 
In-place, O(1) extra space and O(n) time.

Notes:
May contain duplicates. -> Cannot use binary search. -> Brute force.
Reverse in place.

"""
class Solution:
    """
    @param: nums: An integer array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        if len(nums) == 0 or not nums:
            return False
        
        if len(nums) == 1:
            return nums
        
        pivot = -1
        for idx in xrange(len(nums) - 1):
            if nums[idx] > nums[idx + 1]:
                pivot = idx + 1
        
        if pivot == -1:
            return
        
        self.reverseRSA(nums, 0, pivot - 1)
        self.reverseRSA(nums, pivot, len(nums) - 1)
        self.reverseRSA(nums, 0, len(nums) - 1)
        
    def reverseRSA(self, nums, left, right):
        while left < right:
            tmp = nums[left]
            nums[left] = nums[right]
            nums[right] = tmp
            left += 1
            right -= 1
