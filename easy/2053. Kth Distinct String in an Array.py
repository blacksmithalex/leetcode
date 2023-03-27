class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        n = 0
        for a in arr:
            if arr.count(a) == 1:
                n += 1
                if n == k:
                    return a
        return ''

