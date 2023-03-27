class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m, sm = 0, 0 
        for x in nums:
            if x > m:
                sm = m
                m = x
            elif x > sm:
                sm = x
        return (m - 1) * (sm - 1)