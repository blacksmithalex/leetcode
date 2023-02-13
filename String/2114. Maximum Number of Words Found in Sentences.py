class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        mcount = 0
        for s in sentences:
            count = s.count(' ') + 1
            if count > mcount:
                mcount = count
        return mcount