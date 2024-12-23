class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = -1
        r = len(nums) - 1
        while l + 1 != r:
            c = (l + r) // 2
            if nums[c] < nums[c + 1]:
                l = c
            else:
                r = c
        return r