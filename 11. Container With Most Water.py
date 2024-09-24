"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""


class Solution(object):

    def maxArea(self, height):
        left: int = 0
        right: int = len(height) - 1
        max_amount = 0
        if len(height) == 2:
            return min(height[left], height[right]) * (right - left)

        while right > left:
            current = min(height[left], height[right]) * (right - left)
            max_amount = max(max_amount, current)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_amount


# height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# height = [1, 0, 0, 0, 0, 0, 0, 2, 2]
height = [2, 3, 4, 5, 18, 17, 6]

obj = Solution()
print(obj.maxArea(height))
