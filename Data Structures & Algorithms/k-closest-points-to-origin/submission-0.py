class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = [] #stores (distance, point)
        for point in points:
            distance = math.sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(minHeap, (distance, point))

        output = []
        for item in range(k):
            point = heapq.heappop(minHeap)[1]
            output.append(point)
            
        return output