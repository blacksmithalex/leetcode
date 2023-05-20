class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(image)
        for i in range(n):
            line = image[i]
            line = line[::-1]
            line = [(x + 1) % 2 for x in line]
            image[i] = line
        return image    