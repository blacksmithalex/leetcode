class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ma1 = ma2 = 0
        mi1 = mi2 = 10**4
        for x in nums:
            if x > ma1:
                ma2 = ma1
                ma1 = x
            elif x > ma2:
                ma2  = x
            if x < mi1:
                mi2 = mi1 
                mi1 = x
            elif x < mi2:
                mi2 = x
        return ma1 * ma2 - mi1 * mi2
