class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            T = [1] * (n + 1)
            T[0] = 0
            for i in range(3, n + 1):
                T[i] = T[i - 1] + T[i - 2] + T[i - 3]
            return T[n]
