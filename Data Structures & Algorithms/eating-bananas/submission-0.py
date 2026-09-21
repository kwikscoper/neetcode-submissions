class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        res = right

        while left <= right:
            k = left + (right - left) // 2
            
            time = 0
            for pile in piles:
                time += math.ceil(pile / k)

            if time <= h:
                res = k
                right = k - 1
            else:
                left = k + 1

        return res