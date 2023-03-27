class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for a in range(1, n + 1):
            for b in range(a + 1, n + 1):
                c = (a**2 + b**2)**0.5
                if c <= n and int(c) == c:
                    count += 1
        return count * 2