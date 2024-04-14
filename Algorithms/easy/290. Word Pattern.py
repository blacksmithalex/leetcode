class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        data = {}
        words = s.split()
        if len(pattern) != len(words):
            return False
        for i in range(len(pattern)):
            if pattern[i] in data:
                if data[pattern[i]] != words[i]:
                    return False
            else:
                if words[i] in data.values():
                    return False
                data[pattern[i]] = words[i]
        return True

