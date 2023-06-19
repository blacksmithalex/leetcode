class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def traversal(i, j, ind):
            if ind == len(word):
                return True
            if i < 0 or j < 0 or i >= n or j >= m:
                return False
            if board[i][j] != word[ind]:
                return False
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for x, y in directions:
                cur = board[i][j]
                board[i][j] = -1
                if traversal(i + x, j + y, ind + 1):
                    return True
                board[i][j] = cur
        n, m = len(board), len(board[0])
        boardDict = {}
        wordDict = {}
        for i in range(n):
            for j in range(m):
                cur = board[i][j]
                boardDict[cur] = boardDict.get(cur, 0) + 1
        for i in range(len(word)):
            cur = word[i]
            wordDict[cur] = wordDict.get(cur, 0) + 1
        for cur in wordDict:
            if cur not in boardDict or boardDict[cur] < wordDict[cur]:
                return False
        for i in range(n):
            for j in range(m):
                res = traversal(i, j, 0)
                if res:
                    return res
        return False

