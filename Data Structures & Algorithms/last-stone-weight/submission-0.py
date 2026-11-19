import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)
            x, y = -x, -y
            
            if x == y:
                continue
            else:
                heapq.heappush(maxHeap, -abs(x - y))

        return -maxHeap[0] if maxHeap else 0