class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        dp = {}
        def recursion(start, end):
            if start == end:
                return 0
            if (start, end) in dp:
                return dp[(start, end)]
            choice1 = piles[start] - recursion(start + 1, end)
            choice2 = piles[end] - recursion(start, end - 1)
            dp[(start, end)] = max(choice1, choice2)
            return max(choice1, choice2)
        result = recursion(0, len(piles) - 1)
        return result > 0

#Можно возвращать просто True, так как Alice выигрывает всегда