"""
Determine color of a Chessboard Square
"""


class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        if (ord(coordinates[0]) - 96 + int(coordinates[1])) % 2:
            return True
        return False
