class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        res = ''
        for i in range(n):
            for j in range(i + 1, n):
                flag = True
                subseq = s[i:j + 1]
                for x in subseq:
                    if x.islower() and x.upper() not in subseq:
                        flag = False
                    elif x.isupper() and x.lower() not in subseq:
                        flag = False
                if flag and len(subseq) > len(res):
                    res = subseq
        return res
