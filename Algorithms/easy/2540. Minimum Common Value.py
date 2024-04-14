class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
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

        for i in range(len(nums1)):
            ind = lbs(nums2, nums1[i])
            if nums1[i] == nums2[ind]:
                return nums1[i]
        return -1


class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            if nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return -1
