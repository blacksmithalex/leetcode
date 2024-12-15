class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.stream = [None] * n
        self.prev = 0

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        idKey -= 1
        self.stream[idKey] = value
        if self.prev < idKey:
            return []
        else:
            while self.prev < len(self.stream) and self.stream[self.prev] is not None:
                self.prev += 1
            return self.stream[idKey: self.prev]

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)