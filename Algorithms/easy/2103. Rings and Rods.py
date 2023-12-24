class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """
        rods = [set() for _ in range(10)]
        for i in range(0, len(rings) - 1, 2):
            color, pos = rings[i], int(rings[i + 1])
            rods[pos].add(color)
        counts = [len(x) for x in rods]
        return counts.count(3)

