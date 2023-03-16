class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        count = 0
        for d in range(1, min(a, b) + 1):
            if a % d == 0 and b % d == 0:
                count += 1
        return count
