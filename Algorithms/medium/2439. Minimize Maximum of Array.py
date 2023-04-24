class Solution(object):
    def minimizeArrayValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = 0
        result = 0
        for i in range(len(nums)):
            total_sum += nums[i]
            result = max(result, (total_sum + i) // (i + 1))
        return int(result)