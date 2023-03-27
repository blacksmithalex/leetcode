class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        count = 0
        for w in words:
            flag = True
            for l in w:
                if l not in allowed:
                    flag = False
                    break
            if flag:
                count += 1
        return count
