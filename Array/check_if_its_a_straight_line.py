class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x1, y1), (x2, y2) = coordinates[:2]
        return all((x2 - x1) * (y - y2) == (x - x2) * (y2 - y1) for x, y in coordinates)
