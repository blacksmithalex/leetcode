class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0] * n
        s = nums[0]  #сумма всех элементов с начала
        dp[0] = s
        for i in range(1, n):
            s += nums[i]
            dp[i] = min(dp[i - 1], s)

        largest_sum = nums[0]
        s = nums[0]
        for i in range(1, n):
            s += nums[i]
            largest_sum = max(largest_sum, s, s - dp[i - 1])
        return largest_sum