class Solution(object):
    def diagonalPrime(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        def isprime(num):
            if num == 1:
                return False
            for d in range(2, int(sqrt(num)) + 1):
                if num % d == 0:
                    return False
            return True
        mprime = 0
        n = len(nums)
        for i in range(n):
            cell1, cell2 = nums[i][i], nums[i][n - i - 1]
            if isprime(cell1) and cell1 > mprime:
                mprime = cell1
            if isprime(cell2) and cell2 > mprime:
                mprime = cell2
        return mprime