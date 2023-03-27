class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = sorted([int(x) for x in str(num)])
        new1 = num[0] * 10 + num[2]
        new2 = num[1] * 10 + num[3]
        return new1 + new2
