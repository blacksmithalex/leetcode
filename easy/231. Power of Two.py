class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        two = 1
        while two < n:
            two *= 2
        return two == n