# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def get_tree_sum(self, node: TreeNode | None, target_sum, cur_sum: int = 0):
        if not node:
            return False
        tmp_sum = cur_sum + node.val
        if tmp_sum == target_sum and all((not node.left, not node.right)):
            return True
        return self.get_tree_sum(node.left, target_sum, tmp_sum) or self.get_tree_sum(node.right, target_sum, tmp_sum)

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.get_tree_sum(root, targetSum) or False
