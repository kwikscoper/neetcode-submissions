class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        fleets = 0

        i = 0
        while i < len(cars):
            ticks = (target - cars[i][0]) / cars[i][1]
            
            j = i + 1
            while j < len(cars):
                newticks = (target - cars[j][0]) / cars[j][1]
                if newticks <= ticks:
                    cars.pop(j)
                else:
                    break
            fleets += 1

            i += 1

        return fleets