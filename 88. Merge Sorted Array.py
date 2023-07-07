from typing import List


class Solution:
    #  https://leetcode.com/problems/merge-sorted-array/solutions/1176400/best-python-solution-faster-than-99-one-loop-no-splicing-no-special-case-loop/
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        tmp_index = 0
        for i in range(m, m + n):
            nums1[i] = nums2[tmp_index]
            tmp_index += 1
        nums1.sort()


m = 3
n = 3
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
obj = Solution()
obj.merge(nums1, m, nums2, n)
