class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        res = ''
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                cur = s[i] + s[i + 1]
                res += chr(int(cur) + 96)
                i += 3
            else:
                cur = s[i]
                res += chr(int(cur) + 96)
                i += 1
        return res
