class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        uniq = set(sentence)
        return len(uniq) == 26