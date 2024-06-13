class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n = len(arr)
        if n < 3:
            return False
        for i in range(1, n - 1):
            flag = True
            for j in range(i):
                if arr[j] >= arr[j + 1]:
                    flag = False
            for j in range(i, n - 1):
                if arr[j] <= arr[j + 1]:
                    flag = False
            if flag:
                return True
        return False

class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n = len(arr)
        if n < 3:
            return False
        indinc = -1
        inddec = n
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                indinc = i
            else:
                break
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                inddec = i
            else:
                break
        return indinc >= inddec
