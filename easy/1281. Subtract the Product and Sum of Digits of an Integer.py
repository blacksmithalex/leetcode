class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        s, p = 0, 1
        while n != 0:
            last = n % 10
            s += last
            p *= last
            n //= 10
        return p - s