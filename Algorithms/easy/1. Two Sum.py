class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        inds_nums = {}
        for i in range(len(nums)):
            if target - nums[i] in inds_nums:
                return [inds_nums[target - nums[i]], i]
            inds_nums[nums[i]] = i
        return []
