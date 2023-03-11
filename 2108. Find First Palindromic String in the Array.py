class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for w in words:
            if w == w[::-1]:
                return w
        return ''