class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        answer = [0] * len(s)
        indc = [i for i in range(len(s)) if s[i] == c]
        for i in range(len(s)):
            if s[i] != c:
                distm = len(s)
                for j in indc:
                    distm = min(distm, abs(i - j))
                answer[i] = distm
        return answer