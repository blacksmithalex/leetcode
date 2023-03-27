class Solution(object):
    def cellsInRange(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        c1, c2 = ord(s[0]), ord(s[3])
        r1, r2 = int(s[1]), int(s[4])
        for i in range(c1, c2 + 1):
            for j in range(r1, r2 + 1):
                cell = chr(i) + str(j)
                res.append(cell)
        return res