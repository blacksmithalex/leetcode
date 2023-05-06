class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        l1 = moves.count('L') == moves.count('R')
        l2 = moves.count('U') == moves.count('D')
        return l1 and l2