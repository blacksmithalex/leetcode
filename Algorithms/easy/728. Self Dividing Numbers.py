class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for n in range(left, right + 1):
            ncopy = n
            flag = True
            while ncopy != 0:
                last = ncopy % 10
                if last == 0:
                    flag = False
                    break
                if n % last != 0:
                    flag = False
                    break
                ncopy //= 10
            if flag:
                res.append(n)
        return res
