class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [nums[nums[i]]for i in range(len(nums))]
        return ans