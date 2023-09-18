"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        len_nums = len(nums)
        start = 0
        while start < len_nums:
            if nums[start] == 0:
                nums.pop(start)
                nums.append(0)
                len_nums -= 1
            else:
                start += 1

        """
        Do not return anything, modify nums in-place instead.
        """

nums = [0, 1, 0, 3, 12]
nums = [0, 0, 1]

obj = Solution()
obj.moveZeroes(nums)
