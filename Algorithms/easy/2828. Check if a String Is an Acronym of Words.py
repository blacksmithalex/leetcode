class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        acronym = [x[0] for x in words]
        return ''.join(acronym) == s