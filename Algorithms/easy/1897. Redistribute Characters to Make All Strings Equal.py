class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        d = {}
        n = len(words)
        for word in words:
            letters = list(word)
            for l in letters:
                d[l] = d.get(l, 0) + 1
        for l in d:
            if d[l] % n != 0:
                return False
        return True