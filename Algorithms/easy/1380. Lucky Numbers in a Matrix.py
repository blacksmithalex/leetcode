class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        n = len(matrix)
        m = len(matrix[0])
        mrow, mcol = [0] * n, [0] * m
        for i in range(n):
            mrow[i] = min(matrix[i])
        for j in range(m):
            mi = 0
            for i in range(n):
                mi = max(mi, matrix[i][j])
            mcol[j] = mi
        return list(set(mrow) & set(mcol))
