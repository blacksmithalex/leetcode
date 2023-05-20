class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        s_xy = 0
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] != 0:
                    s_xy += 1
        s_xz = 0
        for i in range(n):
            s_xz += max(grid[i])
        s_yz = 0
        for j in range(n):
            sm = 0
            for i in range(n):
                sm = max(sm, grid[i][j])
            s_yz += sm
        return s_xy + s_xz + s_yz
