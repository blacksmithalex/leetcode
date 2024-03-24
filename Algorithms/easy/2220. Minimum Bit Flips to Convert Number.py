class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return (start ^ goal).bit_count()

class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        bstart = bin(start)[2:]
        bgoal = bin(goal)[2:]
        mlen = max(len(bstart), len(bgoal))
        bstart = '0' * (mlen - len(bstart)) + bstart
        bgoal = '0' * (mlen - len(bgoal)) + bgoal
        count = 0
        for i in range(mlen):
            if bstart[i] != bgoal[i]:
                count += 1
        return count