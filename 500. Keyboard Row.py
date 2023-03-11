class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        row1 = set('qwertyuiop')
        row2 = set('asdfghjkl')
        row3 = set('zxcvbnm')
        for w in words:
            setw = set(w.lower())
            if setw.issubset(row1) or setw.issubset(row2) or setw.issubset(row3):
                res.append(w)
        return res
