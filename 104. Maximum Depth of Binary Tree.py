# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def get_depth(self, node: TreeNode):
        if node is None:
            return 0
        return max(1 + self.get_depth(node.left), 1 + self.get_depth(node.right))

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0
        return self.get_depth(root)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        res = 0
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res
