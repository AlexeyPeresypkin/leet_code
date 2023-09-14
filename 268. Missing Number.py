"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_num, min_num = max(nums), min(nums)
        set_range = set(range(0, max_num + 1))
        diff = set_range.difference(set(nums))
        if diff:
            return diff.pop()
        return max_num + 1

    def missingNumber(self, nums: List[int]) -> int:
        sum_nums = sum(nums)
        expected_sum = sum(range(0, len(nums) + 1))
        return expected_sum - sum_nums


nums = [3, 0, 1]

obj = Solution()
print(obj.missingNumber(nums))
