from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_profit = float('inf'), -float('inf')
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, (price - min_price))
        return max_profit



prices = [2, 1, 2, 1, 0, 1, 2]
# prices = [10000, 9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990, 9989, 9988, 9987]
obj = Solution()
print(obj.maxProfit(prices))
