"""
Robot Return to Origin
"""


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x_axis = 0
        y_axis = 0
        table_moves = {
            "U": 1,
            "D": -1,
            "L": -1,
            "R": 1
        }
        for move in moves:
            if move in "LR":
                x_axis += table_moves[move]
            else:
                y_axis += table_moves[move]
        return (x_axis, y_axis) == (0, 0)
