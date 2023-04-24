class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.path = 0
        n, m = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= n or j >= m:
                return False
            if grid[i][j] == 0:
                return True
            self.path += 1
            grid[i][j] = 0
            left = dfs(i - 1, j)
            right = dfs(i + 1, j)
            up = dfs(i, j - 1)
            down = dfs(i, j + 1)
            return left and right and up and down

        cells = 0
        for i in range(n):
            for j in range(m):
                self.path = 0
                if grid[i][j] == 1 and dfs(i, j):
                    cells += self.path

        return cells