class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1 #индекс установки элемента
        n = len(nums) #кол-во элементов
        for j in range(1, n):
            nums[i] = nums[j]
            if nums[i] != nums[i - 1]:
                i += 1
        return i