from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        indexes_for_replaces = []
        count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                indexes_for_replaces.append(i)
                continue
            count += 1
            if indexes_for_replaces:
                ind = indexes_for_replaces.pop(0)
                nums[ind] = nums[i]
                indexes_for_replaces.append(i)
        return count


nums = [0, 1, 2, 2, 3, 0, 4, 2]
obj = Solution()
print(obj.removeElement(nums, 2))
print(nums)
