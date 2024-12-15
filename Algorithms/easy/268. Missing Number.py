class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sprogression = n * (n + 1) // 2
        s = sum(nums)
        return sprogression - s