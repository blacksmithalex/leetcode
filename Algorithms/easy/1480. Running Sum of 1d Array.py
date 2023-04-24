class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        runningSum = [0] * len(nums)
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            runningSum[i] = s
        return runningSum

