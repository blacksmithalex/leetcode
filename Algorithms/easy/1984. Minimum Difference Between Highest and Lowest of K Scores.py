class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0
        nums = sorted(nums)
        mdiff = float('inf')
        for i in range(k - 1, n):
            diff = nums[i] - nums[i - (k - 1)]
            mdiff = min(diff, mdiff)
        return mdiff
