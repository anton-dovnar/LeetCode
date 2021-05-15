class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        length = len(points)
        distance = float('inf')
        result = -1
        if length == 1 and points[0][0] != x and points[0][1] != y:
            return result
        for i in range(length):
            x2, y2 = points[i]
            if x2 == x or y2 == y:
                point_distance = abs(x - x2) + abs(y - y2)
                if point_distance < distance:
                    result = i
                    distance = point_distance
        return result
