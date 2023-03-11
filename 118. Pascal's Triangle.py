class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal = [[1]]
        for i in range(1, numRows):
            cur = [1]
            prev = pascal[-1]
            for j in range(len(prev) - 1):
                cur.append(prev[j] + prev[j + 1])
            cur.append(1)
            pascal.append(cur)
        return pascal
