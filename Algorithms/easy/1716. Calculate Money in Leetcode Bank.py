class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        bound, r = n // 7, n % 7
        main_part = 7 * (1 + bound) * bound // 2 + 21 * bound
        if r == 0:
            return main_part
        r_part = (2 * bound + 1 + r) * r // 2
        return main_part + r_part