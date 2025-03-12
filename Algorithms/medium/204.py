class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # O(nloglogn)
        if n <= 1:
            return 0
        primes = [True] * n
        primes[0], primes[1] = False, False
        for i in range(2, n):
            if primes[i]:
                for j in range(i * i, n, i):
                    primes[j] = False
        return primes.count(True)




