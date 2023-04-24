class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = sorted([word[-1] + word[:-1] for word in s.split()])
        return ' '.join([word[1:] for word in s])
