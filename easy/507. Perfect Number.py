class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return False
        s = 0
        for d in range(1, int(num**0.5) + 1):
            if num % d == 0:
                s += d
                if d != 1 and d != num // d:
                    s += num // d
        return s == num
