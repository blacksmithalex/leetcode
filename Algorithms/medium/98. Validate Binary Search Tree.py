# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def traversal(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            return traversal(node.left, left, node.val) and traversal(node.right, node.val, right)

        return traversal(root, -float('inf'), float('inf'))
