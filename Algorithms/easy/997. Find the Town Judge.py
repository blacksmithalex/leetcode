class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if n == 1:
            return 1
        T = [0] * (n + 1)
        for var in trust:
            T[var[0]] -= 1
            T[var[1]] += 1
        if n - 1 in T:
            return T.index(n - 1)
        return -1
