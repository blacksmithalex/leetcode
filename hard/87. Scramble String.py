class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n = len(s1)
        if len(s2) != n:
            return False
        if s1 == s2:
            return True
        if n == 1:
            return False
        key = s1 + ' ' + s2
        if key in self.mp:
            return self.mp[key]
        for i in range(1, n):
            without_swap = (
                self.isScramble(s1[:i], s2[:i])
                and
                self.isScramble(s1[i:], s2[i:])
            )
            if without_swap:
                return True
            with_swap = (
                self.isScramble(s1[:i], s2[n-i:])
                and
                self.isScramble(s1[i:], s2[:n-i])
            )
            if with_swap:
                return True
        self.mp[key] = False
        return False
    mp = {}