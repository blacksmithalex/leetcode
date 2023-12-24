class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        mcount = 0
        for count in range(1, len(sequence) // len(word) + 1):
            cur = word * count
            if cur in sequence:
                mcount = count
        return mcount