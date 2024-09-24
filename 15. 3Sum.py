"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""


class Solution(object):
    def threeSum(self, nums):
        result = set()
        nums.sort()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum_vars = sum((nums[l], nums[r], nums[i]))
                if sum_vars == 0:
                    result.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif sum_vars < 0:
                    l += 1
                else:
                    r -= 1
        return list(result)


nums = [-1, 0, 1, 2, -1, -4]

obj = Solution()
print(obj.threeSum(nums))
