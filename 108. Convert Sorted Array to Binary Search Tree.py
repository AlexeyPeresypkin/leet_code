# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def make_tree(self, node: TreeNode, arr_left: list, arr_right: list):
        if len(arr_left) == 0:
            pass
        elif len(arr_left) == 1:
            node.left = TreeNode(arr_left[0])
        elif len(arr_left) == 2:
            node.left = TreeNode(arr_left[1])
            node.left.left = TreeNode(arr_left[0])
        elif len(arr_left) == 3:
            node.left = TreeNode(arr_left[1])
            node.left.left = TreeNode(arr_left[0])
            node.left.right = TreeNode(arr_left[2])
        else:
            mid_left = len(arr_left) // 2
            node.left = TreeNode(arr_left[mid_left])
            self.make_tree(node.left, arr_left[:mid_left], arr_left[mid_left + 1:])

        if len(arr_right) == 0:
            pass
        elif len(arr_right) == 1:
            node.right = TreeNode(arr_right[0])
        elif len(arr_right) == 2:
            node.right = TreeNode(arr_right[1])
            node.right.left = TreeNode(arr_right[0])
        elif len(arr_right) == 3:
            node.right = TreeNode(arr_right[1])
            node.right.left = TreeNode(arr_right[0])
            node.right.right = TreeNode(arr_right[2])
        else:
            mid_right = len(arr_right) // 2
            node.right = TreeNode(arr_right[mid_right])
            self.make_tree(node.right, arr_right[:mid_right], arr_right[mid_right + 1:])

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 1:
            return TreeNode(nums[0])
        elif len(nums) == 2:
            return TreeNode(nums[1], TreeNode(nums[0]))
        elif len(nums) == 3:
            return TreeNode(nums[1], TreeNode(nums[0]), TreeNode(nums[2]))
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        self.make_tree(root, nums[:mid], nums[mid + 1:])
        return root

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def cv(node, vals) -> TreeNode:
            if vals:
                mid = len(vals) // 2
                node.val, node.left, node.right = vals[mid], cv(TreeNode(), vals[:mid]), cv(TreeNode(), vals[mid + 1:])
                return node

        return cv(TreeNode(), nums)


nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
obj = Solution()
print(obj.sortedArrayToBST(nums))