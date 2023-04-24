class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev, cur = 0, 1
        for i in range(n):
            prev, cur = cur, prev + cur
        return prev