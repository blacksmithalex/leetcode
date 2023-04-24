class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s1 = set(range(1, len(nums) + 1))
        s2 = set(nums)
        return sorted(s1 - s2)