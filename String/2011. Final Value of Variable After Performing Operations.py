class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        inc = operations.count('++X') + operations.count('X++')
        dec = operations.count('--X') + operations.count('X--')
        return inc - dec