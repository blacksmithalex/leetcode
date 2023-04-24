class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        pos = [i for i in range(1, n // 2 + 1)]
        neg = [-i for i in pos]
        if n % 2 != 0:
            return  pos + [0] + neg
        else:
            return neg + pos
