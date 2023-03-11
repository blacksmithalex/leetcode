class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        mprice = [0] * (len(cost))
        mprice[0], mprice[1] = cost[0], cost[1]
        for i in range(2, len(cost)):
            mprice[i] = min(mprice[i - 1], mprice[i - 2]) + cost[i]
        return min(mprice[-1], mprice[-2])