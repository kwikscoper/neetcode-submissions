class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        
        fleets = 1
        prevticks = (target - cars[0][0]) / cars[0][1]
        for i in range(1, len(cars)):
            ticks = (target - cars[i][0]) / cars[i][1]
            if ticks > prevticks:
                fleets += 1
                prevticks = ticks

        return fleets