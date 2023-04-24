class Solution(object):
    def countPrefixes(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        count = 0
        for x in words:
            if s[:len(x)] == x:
                count += 1
        return count