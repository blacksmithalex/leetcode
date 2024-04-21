class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        for _ in range(k):
            ind = gifts.index(max(gifts))
            gifts[ind] = int(gifts[ind] ** 0.5)
        return sum(gifts)
