class Solution(object):
    def getLongestSubsequence(self, words, groups):
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        last_ind = 0
        res = [words[0]]
        for i in range(1, len(words)):
            if (groups[i] + groups[last_ind]) % 2 != 0:
                res.append(words[i])
                last_ind = i
        return res