class Solution(object):
    def findMinimumOperations(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: int
        """
        i = 0
        while i < min(len(s1), len(s2), len(s3)) and s1[i] == s2[i] == s3[i]:
            i += 1
        if i == 0:
            return -1
        count = len(s1) + len(s2) + len(s3) - 3 * i
        return count
