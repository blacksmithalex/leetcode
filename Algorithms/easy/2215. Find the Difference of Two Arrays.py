class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        answer = [set(), set()]
        nums1, nums2 = set(nums1), set(nums2)
        for n in nums1:
            if n not in nums2:
                answer[0].add(n)
        for n in nums2:
            if n not in nums1:
                answer[1].add(n)
        return answer
