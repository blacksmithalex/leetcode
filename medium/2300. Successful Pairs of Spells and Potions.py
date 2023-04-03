class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        n, m = len(spells), len(potions)
        potions = sorted(potions)
        pairs = []
        for i in range(n):
            l = -1
            r = m - 1
            while l + 1 != r:
                c = (l + r) // 2
                target = spells[i] * potions[c]
                if target < success:
                    l = c
                else:
                    r = c
            if spells[i] * potions[r] >= success:
                pairs.append(m - r)
            else:
                pairs.append(0)
        return pairs

