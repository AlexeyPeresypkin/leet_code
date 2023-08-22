from functools import reduce


class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            num = reduce(lambda x, y: int(x) + int(y), str(num))
        return num


obj = Solution()
print(obj.addDigits(38))
