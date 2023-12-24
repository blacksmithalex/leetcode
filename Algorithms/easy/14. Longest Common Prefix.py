class Solution(object):
    def longestCommonPrefix(self, strs):
        def common_pref(a1, a2):
            if len(a1) > len(a2):
                a1 = a1[:len(a2)]
            else:
                a2 = a2[:len(a1)]
            n = min(len(a1), len(a2))
            cp = ''
            for i in range(n):
                if a1[i] == a2[i]:
                    cp += a1[i]
                else:
                    break
            return cp

        pref = strs[0]
        for word in strs[1:]:
            pref = common_pref(pref, word)
        return pref

