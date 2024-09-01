# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.dfs(root))

    def dfs(self, root):
        if not root:
            return [0, 0]
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        var1 = root.val + l[1] + r[1]
        var2 = max(l[0], l[1]) + max(r[0], r[1])
        return [var1, var2]