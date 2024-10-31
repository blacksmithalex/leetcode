# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def symmetric(p, q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            if p.val == q.val:
                tr1 = symmetric(p.left, q.right)
                tr2 = symmetric(p.right, q.left)
                return tr1 and tr2
            return False

        return symmetric(root.left, root.right)
