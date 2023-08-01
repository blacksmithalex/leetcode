class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        mfreq = max(freq.values())
        for x in freq:
            if freq[x] == mfreq:
                return x