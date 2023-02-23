class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        cr, cl = 0, 0
        for x in s:
            if x == 'R': cr += 1
            if x == 'L': cl += 1
            if cr == cl:
                count += 1
                cr, cl = 0, 0
        return count
