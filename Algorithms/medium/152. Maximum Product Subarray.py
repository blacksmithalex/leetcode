class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev_p = None
        cur_p = 1
        max_p = -float('inf')
        for num in nums: 
            cur_p *= num
            max_p = max(max_p, cur_p)
            if cur_p < 0:
                if prev_p != None:
                    max_p = max(max_p, cur_p // prev_p)
                else:
                    prev_p = cur_p
            elif cur_p == 0:
                cur_p = 1
                prev_p = None
        return max_p