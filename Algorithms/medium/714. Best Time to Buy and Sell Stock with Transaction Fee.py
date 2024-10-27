class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n = len(prices)
        empty = [0] * n
        hold = [0] * n
        hold[0] = -prices[0]
        for i in range(1, n):
            hold[i] = max(hold[i - 1], empty[i - 1] - prices[i])
            empty[i] = max(empty[i - 1], hold[i - 1] + prices[i] - fee)
        return empty[n - 1]