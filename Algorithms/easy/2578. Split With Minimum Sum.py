class Solution(object):
    def splitNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = sorted(str(num))
        num1 = ''.join(num[::2])
        num2 = ''.join(num[1::2])
        return int(num1) + int(num2)
