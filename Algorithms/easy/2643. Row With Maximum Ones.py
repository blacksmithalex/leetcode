class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        ind, count = 0, 0
        for i in range(len(mat)):
            if mat[i].count(1) > count:
                count = mat[i].count(1)
                ind = i
        return [ind, count]
