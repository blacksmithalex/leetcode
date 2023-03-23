class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        Mod = 10 ** 9 + 7
        dp = [0] * len(arr)
        dp[0] = max(dp[0], arr[0])
        for i in range(1, len(dp)):
            dp[i] = max(dp[i - 1] + arr[i], arr[i])
        suff = [0] * len(arr)
        suff[0] = arr[0]
        for i in range(1, len(suff)):
            suff[i] = suff[i - 1] + arr[i]
        preff = [0] * len(arr)
        preff[len(arr) - 1] = arr[-1]
        for i in range(len(arr) - 2, -1, -1):
            preff[i] = preff[i + 1] + arr[i]
        if k == 1:
            return max(max(dp), sum(arr)) % Mod
        return max(max(dp), sum(arr) * k, max(preff) + sum(arr) * (k - 2) + max(suff), max(preff) + max(suff)) % Mod





