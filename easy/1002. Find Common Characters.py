class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        freq = {}
        for key in words[0]:
            freq[key] = freq.get(key, 0) + 1

        for i in range(1, len(words)):
            cur = {}
            for key in words[i]:
                cur[key] = cur.get(key, 0) + 1
            for key in freq:
                if key in cur:
                    freq[key] = min(freq[key], cur[key])
                else:
                    freq[key] = -1
        ans = []
        for key in freq:
            if freq[key] != -1:
                ans += [key] * freq[key]
        return ans