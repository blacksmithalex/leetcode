class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        num = 0
        for h in hours:
            if h >= target:
                num += 1
        return num