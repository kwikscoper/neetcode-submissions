class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        earliestStart = intervals[0][0]
        latestEnd = intervals[0][1]
        output = []
        for start, end in intervals:
            if start <= latestEnd:
                latestEnd = max(latestEnd, end)
            else:
                output.append([earliestStart, latestEnd])
                earliestStart = start
                latestEnd = end

        output.append([earliestStart, latestEnd])

        return output