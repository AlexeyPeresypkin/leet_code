"""
Given an array of points on the X-Y plane points where points[i] = [xi, yi], return the area of the largest triangle that can be formed by any three different points. Answers within 10-5 of the actual answer will be accepted.
"""
from itertools import combinations
from typing import List


class Solution:

    @staticmethod
    def get_square(points: tuple[list]) -> float:
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]
        return abs((x1 * y2 + x2 * y3 + x3 * y1 - y1 * x2 - y2 * x3 - y3 * x1) / 2)

    def largestTriangleArea(self, points: List[List[int]]) -> float:
        return max(map(self.get_square, combinations(points, 3)))


points = [[2, 5], [7, 7], [10, 8], [10, 10], [1, 1]]
print(list(combinations(points, 3)))
obj = Solution()
print(obj.largestTriangleArea(points))
