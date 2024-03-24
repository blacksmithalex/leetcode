class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] < target:
                    count += 1
        return count

class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        N = len(nums)
        nums = sorted(nums)
        count = 0
        l, r = 0, N - 1
        while l < r:
            if nums[l] + nums[r] >= target:
                count += r - l
                r -= 1
            else:
                l += 1
        return N * (N - 1) // 2 - count