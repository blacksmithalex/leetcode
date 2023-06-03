class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        matrix = [[''] * 3 for _ in range(3)]
        n = 1
        for i, j in moves:
            if n % 2 == 1:
                matrix[i][j] = 'A'
            else:
                matrix[i][j] = 'B'
            n += 1
        for i in range(3):
            if matrix[i][0] == matrix[i][1] == matrix[i][2] and  matrix[i][0] != '':
                return matrix[i][0]
        for j in range(3):
            if matrix[0][j] == matrix[1][j] == matrix[2][j] and matrix[0][j] != '':
                return matrix[0][j]
        if matrix[0][0] == matrix[1][1] == matrix[2][2] and matrix[0][0] != '':
            return matrix[0][0]
        if matrix[2][0] == matrix[1][1] == matrix[0][2] and matrix[2][0] != '':
            return matrix[2][0]
        if len(moves) == 9:
            return 'Draw'
        else:
            return 'Pending'