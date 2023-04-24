class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        arr = []
        for i in range(len(names)):
            arr.append([heights[i], names[i]])
        arr = sorted(arr, reverse=True)
        res = [x[1] for x in arr]
        return res
