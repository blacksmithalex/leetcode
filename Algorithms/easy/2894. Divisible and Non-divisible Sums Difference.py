class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        k = n // m
        num2 = (m + k * m) * k // 2
        num1 = (1 + n) * n // 2 - num2
        return num1 - num2
