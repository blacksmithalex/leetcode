class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """

        def todict(word):
            freq = {}
            for letter in word:
                freq[letter] = freq.get(letter, 0) + 1
            return freq

        chars = todict(chars)
        total = 0
        for w in words:
            l = len(w)
            w = todict(w)
            flag = True
            for letter in w:
                if letter not in chars:
                    flag = False
                    break
                if chars[letter] < w[letter]:
                    flag = False
                    break
            if flag:
                total += l
        return total



