class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        start, destination = min(start, destination), max(start, destination)
        forwards = sum(distance[start:destination])
        del distance[start:destination]
        reverse = sum(distance)
        return min(forwards, reverse)