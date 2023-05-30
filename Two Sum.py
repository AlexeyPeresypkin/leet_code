from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums = [item for item in nums if item <= target]
        for i in range(len(nums) - 1):
            for c in range(i + 1, len(nums)):
                if nums[i] + nums[c] == target:
                    return [i, c]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return


nums = [0, 4, 3, 0]
target = 0

obj = Solution()
print(obj.twoSum(nums, target))
