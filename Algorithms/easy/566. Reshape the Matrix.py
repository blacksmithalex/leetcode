class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r * c != len(mat) * len(mat[0]):
            return mat
        a = [[]]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                b = mat[i][j]
                if len(a[-1]) < c:
                    a[-1].append(b)
                else:
                    a.append([b])
        return a