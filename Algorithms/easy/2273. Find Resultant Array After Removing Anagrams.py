class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        def check(word1, word2):
            return sorted(word1) == sorted(word2)
        n = len(words)
        inds = [True] * n
        i = 1
        while i < n:
            while i < n and check(words[i], words[i - 1]):
                inds[i] = False
                i += 1
            i += 1
        return [words[i] for i in range(n) if inds[i]]