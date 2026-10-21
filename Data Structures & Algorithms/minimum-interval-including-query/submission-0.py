class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        active = [] # heap that stores tuple (interval len, interval end)
        sol = {}

        i = 0 # interval index
        intervals.sort()
        for query in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= query:
                start, end = intervals[i]
                heapq.heappush(active, (end - start + 1, end))
                i += 1

            while active and active[0][1] < query:
                heapq.heappop(active)

            sol[query] = active[0][0] if active else -1

        output = []
        for query in queries:
            output.append(sol[query])

        return output