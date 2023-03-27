class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def bs(nums):
            l = -1
            r = len(nums) - 1
            while l + 1 != r:
                c = (l + r) // 2
                if nums[c] > -1:
                    l = c
                else:
                    r = c
            return r
        n_neg = 0
        for nums in grid:
            if nums[-1] < 0:
                n_neg += len(nums) - bs(nums)
        return n_neg
