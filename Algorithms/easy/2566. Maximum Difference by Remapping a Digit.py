class Solution(object):
    def minMaxDifference(self, num):
        """
        :type num: int
        :rtype: int
        """
        digit1 = '9'
        for digit in str(num):
            if digit != '9':
                digit1 = digit
                break
        str_num = str(num)
        num_max = str_num.replace(digit1, '9')
        num_min = str_num.replace(str_num[0], '0')
        return int(num_max) - int(num_min)