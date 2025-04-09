class Solution(object):
    def longestSquareStreak(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        dp = {} 
        res = -1
        for num in nums:
            sqrt_of_num = int(num**0.5)
            if sqrt_of_num * sqrt_of_num == num and sqrt_of_num in dp:
                dp[num] = dp[sqrt_of_num] + 1
                res = max(res, dp[num])
            else:
                dp[num] = 1
        return res