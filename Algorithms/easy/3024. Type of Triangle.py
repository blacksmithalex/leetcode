class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        r1 = nums[0] + nums[1] > nums[2]
        r2 = nums[0] + nums[2] > nums[1]
        r3 = nums[1] + nums[2] > nums[0]
        if r1 and r2 and r3:
            if nums[0] == nums[1] == nums[2]:
                return 'equilateral'
            elif nums[0] == nums[1] or nums[1] == nums[2] or nums[0] == nums[2]:
                return 'isosceles'
            else:
                return 'scalene'
        return 'none'

