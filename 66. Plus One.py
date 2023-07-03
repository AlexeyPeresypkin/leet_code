from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit = int(''.join(map(str, digits))) + 1
        return list(map(int, str(digit)))


digits = [9, 1]
obj = Solution()
obj.plusOne(digits)
