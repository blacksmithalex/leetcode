class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        x, y = 0, 0
        prev = {(0, 0)}
        for p in path:
            if p == 'N': y += 1
            if p == 'S': y -= 1
            if p == 'E': x += 1
            if p == 'W': x -= 1
            if (x, y) in prev:
                return True
            else:
                prev.add((x, y))
        return False