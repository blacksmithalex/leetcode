class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        sign = ''
        if num < 0:
            sign = '-'
            num = abs(num)
        n7 = ''
        while num != 0:
            n7 += str(num % 7)
            num //= 7
        return sign + n7[::-1]