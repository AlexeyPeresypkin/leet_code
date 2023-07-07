from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def get_values(self, l: list, node: TreeNode):
        if node:
            self.get_values(l, node.left)
            l.append(node.val)
            self.get_values(l, node.right)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        if root:
            self.get_values(l, root)
        return l

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []
        cur = root
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                ans.append(cur.val)
                cur = cur.right
        return ans
