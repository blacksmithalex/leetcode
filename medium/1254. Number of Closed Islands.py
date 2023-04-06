class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n, m = len(grid), len(grid[0])
        islands = 0
        def dfs(i, j):
            if i < 0 or j < 0 or i >= n or j >= m:
                return False
            if grid[i][j] == 1:
                return True
            grid[i][j] = 1
            left = dfs(i, j - 1)
            right = dfs(i, j + 1)
            up = dfs(i - 1, j)
            down = dfs(i + 1, j)
            return left and right and up and down

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 and dfs(i, j):
                    islands += 1
        return islands