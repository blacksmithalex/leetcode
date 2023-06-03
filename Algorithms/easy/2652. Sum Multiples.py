class Solution(object):
    def sumOfMultiples(self, n):
        """
        :type n: int
        :rtype: int
        """
        b1, b2, b3 = n // 3, n // 5, n // 7
        b4, b5, b6 = n // 15, n // 21, n // 35
        b7 = n // 105
        s = 3 * (1 + b1) * b1 // 2 + 5 * (1 + b2) * b2 // 2 + 7 * (1 + b3) * b3 // 2
        s -= 15 * (1 + b4) * b4 // 2 + 21 * (1 + b5) * b5 // 2 + 35 * (1 + b6) * b6 // 2
        s += 105 * (1 + b7) * b7 // 2
        return s