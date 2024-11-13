class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        freq_s, freq_t = {}, {}
        for letter in s:
            freq_s[letter] = freq_s.get(letter, 0) + 1
        for letter in t:
            freq_t[letter] = freq_t.get(letter, 0) + 1
        for letter in freq_t:
            if letter not in freq_s:
                return letter
            if freq_s[letter] != freq_t[letter]:
                return letter
