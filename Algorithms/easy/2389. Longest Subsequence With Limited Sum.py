class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
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
        nums = sorted(nums)
        part_s = [0]
        s = 0
        for x in nums:
            s += x
            part_s.append(s)
        ans = []
        for q in queries:
            ind = rbs(part_s, q)
            ans.append(ind)
        return ans
