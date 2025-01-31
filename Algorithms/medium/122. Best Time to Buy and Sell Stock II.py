class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        empty = [0] * n #empty[i] - макс. профит на i-й день, если мы пусты
        hold = [0] * n #hold[i] - макс. профит на i-й день, если мы держим акцию
        hold[0] = -prices[0]
        for i in range(1, n):
            hold[i] = max(hold[i - 1], empty[i - 1] - prices[i])
            empty[i] = max(empty[i - 1], hold[i - 1] + prices[i])
        return empty[n - 1]