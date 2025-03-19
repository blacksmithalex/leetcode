class Solution(object):
    def minImpossibleOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #1 = 0001
        #2 = 0010
        #4 = 0100
        #8 = 1000
        #15 = 1 | 2 | 4 | 8
        nums = set(nums) #O(n)
        two = 1
        while two in nums: #O(1)
            two <<= 1
        return two