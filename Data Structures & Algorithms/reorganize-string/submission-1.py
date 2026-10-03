class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = defaultdict(int)
        for char in s:
            counts[char] += 1

        maxHeap = []
        for char in counts:
            heapq.heappush(maxHeap, (-1 * counts[char], char))

        output = []
        queue = deque() #characters come in on one cycle, leave the next, 1 cycle delay
        while maxHeap or queue:
            if not maxHeap:
                return ""
            
            currRem, currChar = heapq.heappop(maxHeap)
            currRem += 1
            output.append(currChar)

            if queue:
                newRem, newChar = queue.popleft()
                heapq.heappush(maxHeap, (newRem, newChar))

            if currRem:
                queue.append((currRem, currChar))

        return "".join(output)