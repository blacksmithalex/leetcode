class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def valrow(i, board):
            elems = board[i]
            enums = [int(x) for x in elems if x != '.']
            return len(enums) == len(set(enums))
        def valcol(j, board):
            elems = []
            for i in range(9):
                elems.append(board[i][j])
            enums = [int(x) for x in elems if x != '.']
            return len(enums) == len(set(enums))
        def valsquare(i, j, board):
            elems = []
            for i1 in range(i, i + 3):
                for j1 in range(j, j + 3):
                    elems.append(board[i1][j1])
            enums = [int(x) for x in elems if x != '.']
            return len(enums) == len(set(enums))
        for i in range(9):
            if not valrow(i, board):
                return False
        for j in range(9):
            if not valcol(j, board):
                return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not valsquare(i, j, board):
                    return False
        return True