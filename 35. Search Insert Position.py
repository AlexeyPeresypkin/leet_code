from typing import List


class Solution(object):

    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
        if left + 1 > len(nums):
            return left
        if right < 0:
            return 0
        if nums[left] < target:
            return left + 1
        return left

    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return left


obj = Solution()
nums = [1, 2, 4, 6, 7]
nums = [1, 3, 5, 6]
print(obj.searchInsert(nums, 7))
