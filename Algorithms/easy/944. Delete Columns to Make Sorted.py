class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        count = 0
        for j in range(len(strs[0])):
            for i in range(len(strs) - 1):
                if strs[i][j] > strs[i + 1][j]:
                    count += 1
                    break
        return count



