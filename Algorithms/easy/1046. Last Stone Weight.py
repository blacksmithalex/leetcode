class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while len(stones) > 1:
            stones = sorted(stones)
            x = stones.pop()
            y = stones.pop()
            if x != y:
                stones.append(abs(x - y))
        if len(stones) == 0:
            return 0
        else:
            return stones[0]