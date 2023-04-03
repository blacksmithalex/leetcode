class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        three = 1
        while three < n:
            three *= 3
        return three == n