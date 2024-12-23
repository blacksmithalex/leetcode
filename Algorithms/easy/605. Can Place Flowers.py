class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        inds_flow = [i for i in range(len(flowerbed)) if flowerbed[i] == 1]
        if len(inds_flow) == 0:
            return (len(flowerbed) + 1) // 2 >= n
        count = inds_flow[0] // 2
        for i in range(len(inds_flow) - 1):
            count += (inds_flow[i + 1] - inds_flow[i] - 2) // 2
        count += (len(flowerbed) - inds_flow[-1] - 1) // 2
        return count >= n

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                count += 1
        return count >= n