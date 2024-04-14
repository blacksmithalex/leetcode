class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = [x[::-1] for x in s.split()]
        return ' '.join(s)
