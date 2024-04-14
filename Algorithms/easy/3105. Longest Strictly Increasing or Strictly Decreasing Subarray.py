class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def incsub(nums):
            count, countm = 1, 1
            for i in range(len(nums) - 1):
                if nums[i] < nums[i + 1]:
                    count += 1
                    if count > countm:
                        countm = count
                else:
                    count = 1
            return countm
        return max(incsub(nums), incsub(nums[::-1]))