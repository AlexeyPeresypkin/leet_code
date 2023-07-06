class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        first, last = 1, x
        while first <= last:
            mid = first + (last - first) // 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 > x:
                last = mid - 1
            elif mid ** 2 < x:
                first = mid + 1
        return last


x = 101
obj = Solution()
print(obj.mySqrt(x))
