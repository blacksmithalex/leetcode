class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        el_sum = sum(nums)
        dig_sum = 0
        for x in nums:
            dig_sum += sum([int(x) for x in str(x)])
        return abs(el_sum - dig_sum)
