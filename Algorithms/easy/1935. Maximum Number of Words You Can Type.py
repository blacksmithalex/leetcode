class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        count = 0
        text = text.split()
        for word in text:
            flag = True
            for l in word:
                if l in brokenLetters:
                    flag = False
                    break
            if flag:
                count += 1
        return count

