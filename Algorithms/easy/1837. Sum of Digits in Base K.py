class Solution(object):
    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        s = 0
        while n != 0:
            s += n % k
            n //= k
        return s