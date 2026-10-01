class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #need dijkstra
        network_map = defaultdict(list)
        for src, dst, weight in times:
            network_map[src].append((weight, dst))

        priority_queue = [(0, k)]
        shortest_time = {}
        while priority_queue:
            curr_time, curr_node = heapq.heappop(priority_queue)
            if curr_node in shortest_time:
                continue
            
            shortest_time[curr_node] = curr_time
            for next_time, next_node in network_map[curr_node]:
                if next_node not in shortest_time:
                    heapq.heappush(priority_queue, (curr_time + next_time, next_node))

        if len(shortest_time) < n:
            return -1
        
        return max(shortest_time.values())