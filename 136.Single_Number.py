class Solution(object):
    def singleNumber(self, nums) -> int:
        x = 0
        for i in nums:
            x ^= i
        return x


solution = Solution()
print(solution.singleNumber([2, 2, 1]))
print(solution.singleNumber([4, 1, 2, 1, 2]))
