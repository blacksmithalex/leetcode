class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        count = 0
        for n in range(left, right + 1):
            if bin(n)[2:].count('1') in primes:
                count += 1
        return count
