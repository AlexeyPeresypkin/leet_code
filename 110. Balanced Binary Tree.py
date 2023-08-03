# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:

    def get_depth(self, node: TreeNode, depth):
        if node:
            return max(self.get_depth(node.left, depth + 1), self.get_depth(node.right, depth + 1))
        return depth

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        diff = abs(self.get_depth(root.left, 0) - self.get_depth(root.right, 0))
        return all((diff <= 1, self.isBalanced(root.left), self.isBalanced(root.right)))


n_8 = TreeNode(8)
n_7 = TreeNode(4, n_8)
n_6 = TreeNode(5)
n_5 = TreeNode(2, n_7, n_6)

n_4 = TreeNode(6)
n_3 = TreeNode(3, n_4)
n_2 = TreeNode(1, n_5, n_3)

obj = Solution()
print(obj.isBalanced(n_2))
