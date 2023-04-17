class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target > nums[-1]:
            return len(nums)
        l = -1
        r = len(nums) - 1
        while l + 1 != r:
            c = (l + r) // 2
            if nums[c] < target:
                l = c
            else:
                r = c
        return r