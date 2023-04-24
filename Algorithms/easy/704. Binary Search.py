class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = -1
        r = len(nums) - 1
        while l + 1 != r:
            c = (l + r) // 2
            if nums[c] < target:
                l = c
            else:
                r = c
        if nums[r] == target:
            return r
        else:
            return -1