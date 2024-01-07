class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leftsum, rightsum = 0, sum(nums)
        n = len(nums)
        answer = [0] * n
        for i in range(n):
            rightsum -= nums[i]
            answer[i] = abs(leftsum - rightsum)
            leftsum += nums[i]
        return answer