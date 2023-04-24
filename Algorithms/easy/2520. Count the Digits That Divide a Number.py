class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        numcopy = num
        while numcopy != 0:
            last = numcopy % 10
            if num % last == 0:
                count += 1
            numcopy //= 10
        return count