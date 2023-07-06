class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        fib_1, fib_2 = 1, 2
        while n > 3:
            fib_1, fib_2 = fib_2, fib_1 + fib_2
            n -= 1
        return fib_1 + fib_2


n = 13
obj = Solution()
print(obj.climbStairs(n))
