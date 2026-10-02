class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = defaultdict(int)
        for task in tasks:
            counts[task] += 1

        maxFreqHeap = []
        for task in counts:
            heapq.heappush(maxFreqHeap, -1 * counts[task]) #stores counts remaining for a specific task, negative so most remaining is on top

        queue = deque() #stores ()
        time = 0
        while maxFreqHeap or queue: #stuff in heap is ready to run, stuff is queue is on cooldown
            time += 1
            if maxFreqHeap:
                remaining = heapq.heappop(maxFreqHeap) + 1
                if remaining:
                    queue.append((remaining, time + n)) #cannot run again until newTime = time + n
            
            if queue and queue[0][1] <= time:
                heapq.heappush(maxFreqHeap, queue.popleft()[0])

        return time