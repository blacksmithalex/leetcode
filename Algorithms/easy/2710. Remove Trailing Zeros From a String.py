class Solution(object):
    def removeTrailingZeros(self, num):
        """
        :type num: str
        :rtype: str
        """
        ind = len(num) - 1
        while num[ind] == '0':
            ind -= 1
        return num[:ind + 1]
