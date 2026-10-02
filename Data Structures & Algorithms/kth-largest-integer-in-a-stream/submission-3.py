class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minKElements = []
        self.k = k
        for num in nums:
            heapq.heappush(self.minKElements, num)
            if len(self.minKElements) > k:
                heapq.heappop(self.minKElements)

    def add(self, val: int) -> int:
        heapq.heappush(self.minKElements, val)
        if len(self.minKElements) > self.k:
            heapq.heappop(self.minKElements)
        return self.minKElements[0]