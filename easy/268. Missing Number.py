class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = max(nums)
        s_nums = sum(nums)
        s_to_m = (1 + m) * m // 2
        if s_nums == s_to_m:
            if 0 in nums:
                return m + 1
            else:
                return 0
        else:
            return s_to_m - s_nums