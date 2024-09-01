class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, 0
        jumps = 0
        while right < len(nums) - 1:
            newright = 0
            for i in range(left, right + 1):
                newright = max(newright, i + nums[i])
            left = right + 1
            right = newright
            jumps += 1
        return jumps
