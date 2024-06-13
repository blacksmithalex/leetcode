class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = ''
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                res += s[i].lower()
        return res == res[::-1]