class Solution(object):
    def oddCells(self, m, n, indices):
        """
        :type m: int
        :type n: int
        :type indices: List[List[int]]
        :rtype: int
        """
        mat = [[0] * n for x in range(m)] 
        for i in indices:
            for j in range(n):
                mat[i[0]][j] += 1
        for i in indices:
            for j in range(m):
                mat[j][i[1]] += 1
        count = 0
        for i in mat:
            for j in i:
                if j % 2 == 1:
                    count += 1
        return count