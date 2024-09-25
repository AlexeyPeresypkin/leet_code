class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


root6 = TreeNode(6)
root7 = TreeNode(7)
root9 = TreeNode(9)
root5 = TreeNode(5, root6, root7)
root4 = TreeNode(4)
root2 = TreeNode(2, root4, root5)
root8 = TreeNode(8, root9)
root3 = TreeNode(3, right=root8)
root1 = TreeNode(1, root2, root3)


class Solution(object):
    def postorderTraversal(self, root):
        stack = [root]
        result = []
        if not root:
            return []

        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result[::-1]


solution = Solution()
print(solution.postorderTraversal(root1))
