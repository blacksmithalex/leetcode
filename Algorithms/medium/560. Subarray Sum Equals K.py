class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        pref = {}
        count = 0
        s = 0
        for x in nums:
            s += x
            if s == k:
                count += 1
            if s - k in pref:
                count += pref[s - k]
            pref[s] = pref.get(s, 0) + 1
        return count