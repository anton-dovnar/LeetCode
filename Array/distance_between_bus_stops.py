class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        st = min(start, destination)
        stop = max(start, destination)
        return min(sum(distance[st:stop]), sum(distance) - sum(distance[st:stop]))
