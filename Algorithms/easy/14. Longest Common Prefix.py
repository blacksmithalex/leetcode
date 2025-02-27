class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        def PairPrefix(word1, word2):
            min_len = min(len(word1), len(word2))
            i = 0
            while i < min_len and word1[i] == word2[i]:
                i += 1
            return word1[:i]
        res = strs[0]
        for word2 in strs[1:]:
            res = PairPrefix(res, word2)
        return res