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
                curletter = board[i][j]
                board[i][j] = -1
                if traversal(i + x, j + y, ind + 1):
                    return True
                board[i][j] = curletter

        n, m = len(board), len(board[0])
        boardDict, wordDict = {}, {}
        for i in range(n):
            for j in range(m):
                curletter = board[i][j]
                boardDict[curletter] = boardDict.get(curletter, 0) + 1
        for letter in word:
            wordDict[letter] = wordDict.get(letter, 0) + 1
        for letter in wordDict:
            if letter not in boardDict or boardDict[letter] < wordDict[letter]:
                return False
        for i in range(n):
            for j in range(m):
                if traversal(i, j, 0):
                    return True
        return False