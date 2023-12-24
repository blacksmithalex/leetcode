class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        scopy = ''
        for l in s:
            if l == 'i':
                scopy = scopy[::-1]
            else:
                scopy += l
        return scopy