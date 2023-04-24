class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        letters = sorted('QWERTYUIOPASDFGHJKLZXCVBNM')
        res = ''
        while columnNumber != 0:
            res += letters[(columnNumber - 1) % 26]
            columnNumber = (columnNumber - 1) // 26
        return res[::-1]