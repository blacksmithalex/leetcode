class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        mchet = 0
        mnechet = 0
        for x in position:
            if x % 2 == 0:
                mchet += 1
            else:
                mnechet += 1
        return min(mchet, mnechet)