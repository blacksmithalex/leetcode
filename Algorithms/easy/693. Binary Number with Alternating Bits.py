class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        bn = bin(n)[2:]
        for i in range(len(bn) - 1):
            if bn[i] == bn[i + 1]:
                return False
        return True
