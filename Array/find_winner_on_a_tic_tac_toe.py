class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[0, 0, 0] for _ in range(3)]
        for i, move in enumerate(moves):
            row, col = move
            if i % 2:
                board[row][col] = -1
            else:
                board[row][col] = 1

        for row_idx in range(3):
            if (x := sum(board[row_idx])) in {-3, 3}:
                return (0, 'B', 0, 'A')[x]
            if (y := sum([board[i][row_idx] for i in range(3)])) in {-3, 3}:
                return (0, 'B', 0, 'A')[y]

        if (diag := sum([board[0][0], board[1][1], board[2][2]])) in {-3, 3}:
            return (0, 'B', 0, 'A')[diag]
        if (rev_diag := sum([board[0][2], board[1][1], board[2][0]])) in {-3, 3}:
            return (0, 'B', 0, 'A')[rev_diag]

        if 0 in set(sum(board, [])):
            return 'Pending'
        return 'Draw'
