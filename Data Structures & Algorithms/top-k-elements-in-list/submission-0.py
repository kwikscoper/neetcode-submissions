class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        topKElements = []
        for num in counts:
            heapq.heappush(topKElements, (counts[num], num))
            if len(topKElements) > k:
                heapq.heappop(topKElements)

        output = [item[1] for item in topKElements]
        return output