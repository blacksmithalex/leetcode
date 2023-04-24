class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = 0
        r = x + 1
        while l + 1 != r:
            c = (l + r) // 2
            if c * c > x:
                r = c
            else:
                l = c
        return l