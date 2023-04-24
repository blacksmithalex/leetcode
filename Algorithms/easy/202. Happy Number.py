class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        prev = {n}
        while n != 1:
            n = sum([int(x)**2 for x in str(n)])
            if n in prev:
                break
            prev.add(n)
        return n == 1