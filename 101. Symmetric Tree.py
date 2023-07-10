from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        elif (not root.left and root.right) or (not root.right and root.left):
            return False
        stack_left = []
        stack_right = []
        cur_left = root.left
        cur_right = root.right
        while (stack_left and stack_right) or (cur_left and cur_right):
            if (cur_left is None and cur_right) or (cur_right is None and cur_left):
                return False
            if cur_left and cur_right:
                if cur_left.val != cur_right.val:
                    return False
                stack_left.append(cur_left.right)
                stack_right.append(cur_right.left)
                cur_left = cur_left.left
                cur_right = cur_right.right
            else:
                cur_left = stack_left.pop()
                cur_right = stack_right.pop()
        if any((stack_left, stack_right, cur_left, cur_right)):
            return False
        return True


rr1_l = TreeNode(4)
rr1_r = TreeNode(3)
rl1_r = TreeNode(4)
rl1_l = TreeNode(3)
rl1 = TreeNode(2, rl1_l, rl1_r)
rr1 = TreeNode(2, rr1_l, rr1_r)
root = TreeNode(1, rl1, rr1)
obj = Solution()
print(obj.isSymmetric(root))
