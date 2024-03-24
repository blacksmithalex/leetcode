class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
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
        arr = sorted(arr)
        for i in range(len(arr)):
            ind = rbs(arr, 2 * arr[i])
            if i != ind and arr[i] * 2 == arr[ind]:
                return True
        return False
