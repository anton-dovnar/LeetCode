class Solution:
    def isPathCrossing(self, path: str) -> bool:
        directions = {
            "N": (0, 1),
            "S": (0, -1),
            "W": (-1, 0),
            "E": (1, 0),
        }
        visited = {(0, 0)}
        current_point = (0, 0)
        for direction in path:
            x, y = directions[direction]
            current_point = current_point[0] + x, current_point[1] + y
            if current_point in visited:
                return True
            visited.add(current_point)
        return False
