class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        box = {}
        for ball in range(lowLimit, highLimit + 1):
            sum_of_digits = sum([int(x) for x in str(ball)])
            box[sum_of_digits] = box.get(sum_of_digits, 0) + 1
        return max(box.values())