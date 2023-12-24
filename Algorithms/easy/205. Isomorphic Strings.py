class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sch, tch = {}, {}
        for i in range(len(s)):
            sch[s[i]] = sch.get(s[i], []) + [i]
        for i in range(len(t)):
            tch[t[i]] = tch.get(t[i], []) + [i]
        for ch1 in sch:
            flag = False
            for ch2 in tch:
                if sch[ch1] == tch[ch2]:
                    flag = True
                    break
            if flag == False:
                return False
        return True
