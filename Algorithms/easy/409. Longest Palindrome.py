class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = {}
        for letter in s:
            freq[letter] = freq.get(letter, 0) + 1
        flag = False
        count = 0
        for letter in freq:
            if freq[letter] % 2 == 0:
                count += freq[letter]
            else:
                count += freq[letter] - 1
                flag = True
        return count + int(flag)