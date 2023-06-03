class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """

        def lbs(a, x):
            l = -1
            r = len(a) - 1
            while l + 1 != r:
                c = (l + r) // 2
                if a[c] < x:
                    l = c
                else:
                    r = c
            return r

        def rbs(a, x):
            l = 0
            r = len(a)
            while l + 1 != r:
                c = (l + r) // 2
                if a[c] > x:
                    r = c
                else:
                    l = c
            return l

        arr2 = sorted(arr2)
        count = 0
        for x in arr1:
            i1, i2 = lbs(arr2, x), rbs(arr2, x)
            if abs(x - arr2[i1]) > d and abs(x - arr2[i2]) > d:
                count += 1
        return count















