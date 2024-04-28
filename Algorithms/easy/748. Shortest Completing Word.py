class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        def todict(word):
            freq = {}
            for letter in word:
                freq[letter] = freq.get(letter, 0) + 1
            return freq
        sh_comp_word = ''
        licensePlate = [x.lower() for x in list(licensePlate) if x.isalpha()]
        licensePlate = todict(licensePlate)
        for word in words:
            dword = todict(word)
            flag = True
            for letter in licensePlate:
                if letter not in dword:
                    flag = False
                    break
                if dword[letter] < licensePlate[letter]:
                    flag = False
                    break
            if flag:
                if len(sh_comp_word) == 0:
                    sh_comp_word = word
                elif len(word) < len(sh_comp_word):
                    sh_comp_word = word
        return sh_comp_word
