class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        cur = [1]
        newcur = [1]
        for i in range(1, rowIndex + 1):
            newcur = [1]
            for j in range(len(cur) - 1):
                newcur.append(cur[j] + cur[j + 1])
            newcur.append(1)
            cur = newcur
        return newcur