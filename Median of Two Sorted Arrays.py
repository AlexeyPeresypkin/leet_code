from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        while True:
            if len(nums1) == 0:
                merged += nums2[::-1]
                break
            elif len(nums2) == 0:
                merged += nums1[::-1]
                break
            try:
                if nums2[-1] > nums1[-1]:
                    merged.append(nums2.pop())
                else:
                    merged.append(nums1.pop())
            except IndexError:
                continue
        if len(merged) % 2:
            return float(merged[len(merged) // 2])
        else:
            return float(merged[len(merged) // 2] + merged[len(merged) // 2 - 1]) / 2


obj = Solution()
nums1 = [1, 3]
nums2 = [2, 7]
print(obj.findMedianSortedArrays(nums1, nums2))
