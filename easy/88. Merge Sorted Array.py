class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1copy = nums1[:m]
        i, j = 0, 0
        while not (i == m and j == n):
            if i != m and j != n:
                if nums1copy[i] < nums2[j]:
                    nums1[i + j] = nums1copy[i]
                    i += 1
                else:
                    nums1[i + j] = nums2[j]
                    j += 1
            elif i != m and j == n:
                nums1[i + j] = nums1copy[i]
                i += 1
            elif i == m and j != n:
                nums1[i + j] = nums2[j]
                j += 1