class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        n, m = len(grid), len(grid[0])
        nislands = 0
        def dfs(i, j, grid):
            if i >= 0 and j >= 0 and i < n and j < m and grid[i][j] == '1':
                grid[i][j] = '0'
                dfs(i - 1, j, grid)
                dfs(i + 1, j, grid)
                dfs(i, j - 1, grid)
                dfs(i, j + 1, grid)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    nislands += 1
                    dfs(i, j, grid)
        return nislands
