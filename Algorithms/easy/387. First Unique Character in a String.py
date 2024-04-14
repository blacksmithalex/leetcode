class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        uniq = set(s)
        ind_m = float('inf')
        for letter in uniq:
            if s.count(letter) == 1:
                ind_m = min(ind_m, s.find(letter))
        if ind_m == float('inf'):
            return -1
        else:
            return ind_m
