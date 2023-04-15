class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        s = 0
        n, m = len(grid), len(grid[0])
        grid = [sorted(line) for line in grid]
        for j in range(m):
            localm = 0
            for i in range(n):
                localm = max(localm, grid[i][j])
            s += localm
        return s
