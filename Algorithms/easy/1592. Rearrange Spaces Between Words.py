class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """
        spaces = text.count(' ')
        words = text.split()
        if len(words) == 1:
            return words[0] + ' ' * spaces
        between = spaces // (len(words) - 1)
        r = spaces % (len(words) - 1)
        res = (' ' * between).join(words)
        res += ' ' * r
        return res