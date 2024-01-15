class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        cities = set()
        out_cities = set()
        for A, B in paths:
            cities.add(A)
            cities.add(B)
            out_cities.add(A)
        return list(cities - out_cities)[0]

