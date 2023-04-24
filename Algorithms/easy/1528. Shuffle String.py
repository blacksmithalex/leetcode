class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        scopy = list(s)
        for i in range(len(s)):
            scopy[indices[i]] = s[i]
        scopy = ''.join(scopy)
        return scopy
