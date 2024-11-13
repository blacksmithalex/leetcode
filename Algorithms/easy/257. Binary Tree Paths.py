# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        paths = []

        def traversal(root, path=''):
            if not root:
                return
            if path:
                path += '->' + str(root.val)
            else:
                path = str(root.val)
            if not root.left and not root.right:
                paths.append(path)
                return
            traversal(root.left, path)
            traversal(root.right, path)

        traversal(root)
        return paths



