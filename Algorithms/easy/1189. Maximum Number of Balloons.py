class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        freq = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        for x in text:
            if x in freq:
                freq[x] += 1
        freq['l'] //= 2
        freq['o'] //= 2
        return min(freq.values())