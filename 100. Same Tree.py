from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        cur_p = p
        cur_q = q
        stack_p = []
        stack_q = []
        while (cur_p and cur_q) or (stack_p and stack_q):
            if cur_p and cur_q:
                if cur_p.val != cur_q.val:
                    return False
                stack_p.append(cur_p.right)
                stack_q.append(cur_q.right)
                cur_p = cur_p.left
                cur_q = cur_q.left
            else:
                if cur_p != cur_q:
                    return False
                cur_p = stack_p.pop()
                cur_q = stack_q.pop()
        if (cur_p is None and cur_q) or (cur_q is None and cur_p):
            return False
        elif (stack_p and not stack_q) or (stack_q and not stack_p):
            return False
        return True


pl_1 = TreeNode(3)
pr_1 = TreeNode(4)
p = TreeNode(2, pl_1, pr_1)

qr_1 = TreeNode(4)
q = TreeNode(2, None, qr_1)

obj = Solution()
print(obj.isSameTree(p, q))
