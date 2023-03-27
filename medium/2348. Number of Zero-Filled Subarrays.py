class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_zero_subarrays = current_zero_subarrays = 0
        for num in nums:
            if num == 0:
                current_zero_subarrays += 1
                total_zero_subarrays += current_zero_subarrays
            else:
                current_zero_subarrays = 0

        return total_zero_subarrays