class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = [1] + nums + [1]
        n = len(nums)
        suff = [1] * n
        pref = [1] * n
        for i in range(1, n):
            pref[i] = pref[i - 1] * nums[i]
        for i in range(n - 2, -1, -1):
            suff[i] = suff[i + 1] * nums[i]
        res = [0] * n
        for i in range(1, n - 1):
            res[i] = pref[i - 1] * suff[i + 1]
        return res[1:-1]
        
        