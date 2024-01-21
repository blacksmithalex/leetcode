class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        scopy = ''
        for i in range(0, len(s) - 1, 2):
            scopy += s[i]
            scopy += chr(ord(s[i]) + int(s[i + 1]))
        if len(s) % 2 != 0:
            scopy += s[-1]
        return scopy