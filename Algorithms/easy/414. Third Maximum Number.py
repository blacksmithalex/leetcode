class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        INF = min(nums) - 1
        m1, m2, m3 = INF, INF, INF
        for n in nums:
            if n > m1:
                m2, m3 = m1, m2
                m1 = n
            elif n > m2 and n != m1:
                m3 = m2
                m2 = n
            elif n > m3 and n != m1 and n != m2:
                m3 = n
        if m3 != INF:
            return m3
        return m1
