class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        nbars = 0
        nstars = 0
        for l in s:
            if l == '*' and nbars != 1:
                nstars += 1
            elif l == '|':
                nbars = (nbars + 1) % 2
        return nstars