class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        degs = [0] * (len(edges) + 2)
        for var in edges:
            degs[var[0]] += 1
            degs[var[1]] += 1
        return degs.index(len(edges))