# Definition for a binary tree node.
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

    def preorderTraversal(self, root: TreeNode):
        """recursive"""
        def recursive_func(tree_node: TreeNode):
            if tree_node.left:
                result.append(tree_node.left.val)
                recursive_func(tree_node.left)
            if tree_node.right:
                result.append(tree_node.right.val)
                recursive_func(tree_node.right)

        result = [root.val]
        recursive_func(root)
        return result

    def preorderTraversal(self, root: TreeNode):
        """Stack"""
        if root is None: return []
        stack = [root]
        result = []
        # result.append(root.val)
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

solution = Solution()
print(solution.preorderTraversal(root1))
