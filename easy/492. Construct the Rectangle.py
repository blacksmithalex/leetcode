class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        div1, div2 = 1, area
        for d in range(1, int(area**0.5) + 1):
            if area % d == 0:
                if area // d - d < div2 - div1:
                    div1, div2 = d, area // d
        return [div2, div1]