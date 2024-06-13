class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return sorted([x**2 for x in nums])

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [0] * n
        indneg = -1
        for i in range(n):
            if nums[i] >= 0:
                break
            indneg = i
        i, j, pos = indneg, indneg + 1, 0
        while i >= 0 and j < n:
            if nums[i]**2 < nums[j]**2:
                res[pos] = nums[i]**2
                i -= 1
            else:
                res[pos] = nums[j]**2
                j += 1
            pos += 1
        while i >= 0:
            res[pos] = nums[i]**2
            pos += 1
            i -= 1
        while j < n:
            res[pos] = nums[j]**2
            pos += 1
            j += 1
        return res