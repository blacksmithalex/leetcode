class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def lbs(a, x):
            l = -1
            r = len(a) - 1
            while l + 1 != r:
                c = (l + r) // 2
                if a[c] < x:
                    l = c
                else:
                    r = c
            return r
        def rbs(a, x):
            l = 0
            r = len(a)
            while l + 1 != r:
                c = (l + r) // 2
                if a[c] > x:
                    r = c
                else:
                    l = c
            return l
        ind1, ind2 = rbs(nums, -1), lbs(nums, 1)
        if nums[ind1] > -1: ind1 -= 1
        neg = ind1 + 1
        if nums[ind2] < 1: ind2 += 1
        pos = len(nums) - ind2
        return max(neg, pos)