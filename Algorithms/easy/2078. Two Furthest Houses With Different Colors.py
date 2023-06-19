class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        color1, color2 = colors[0], colors[-1]
        i, j = 0, len(colors) - 1
        while colors[i] ==  color2:
            i += 1
        while colors[j] == color1:
            j -= 1
        return max(len(colors) - 1 - i, j)