class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def lbs(nums, target):
            l = -1
            r = len(nums) - 1
            while l + 1 != r:
                c = (l + r) // 2
                if nums[c] < target:
                    l = c
                else:
                    r = c
            return r
        def rbs(nums, target):
            l = 0
            r = len(nums)
            while l + 1 != r:
                c = (l + r) // 2
                if nums[c] > target:
                    r = c
                else:
                    l = c
            return l
        nums = sorted(nums)
        indl, indr = lbs(nums, target), rbs(nums, target)
        if nums[indl] != target:
            return []
        return [x for x in range(indl, indr + 1)]





