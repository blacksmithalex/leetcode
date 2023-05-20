class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        s = 0
        n = len(mat)
        for i in range(n):
            for j in range(n):
                if i == j or i + j == n - 1:
                    s += mat[i][j]
        return s