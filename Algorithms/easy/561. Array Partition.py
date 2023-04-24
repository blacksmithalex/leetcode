class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        msum = 0
        for i in range(0, len(nums), 2):
            msum += nums[i]
        return msum