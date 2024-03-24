class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        mdist = 0
        bN = bin(n)[2:]
        prev, cur = float('inf'), 0
        while cur < len(bN):
            if bN[cur] == '1':
                mdist = max(mdist, cur - prev)
                prev = cur
            cur += 1
        return mdist