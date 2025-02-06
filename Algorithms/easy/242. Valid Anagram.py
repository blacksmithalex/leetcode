class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        freq_s, freq_t = {}, {}
        for letter in s:
            freq_s[letter] = freq_s.get(letter, 0) + 1
        for letter in t:
            freq_t[letter] = freq_t.get(letter, 0) + 1
        return freq_s == freq_t