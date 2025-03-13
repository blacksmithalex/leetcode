class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        def factorial(n):
            res = 1
            for i in range(1, n + 1):
                res *= i
            return res

        def comb(n, k):
            return factorial(n) // (factorial(n - k) * factorial(k))

        return comb(m + n - 2, n - 1)

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def comb(n, k):
            bound_max = max(n - k, k)
            bound_min = min(n - k, k)
            res = 1
            for num in range(bound_max + 1, n + 1):
                res *= num
            for num in range(1, bound_min + 1):
                res //= num
            return res
        
        return comb(m + n - 2, n - 1)