class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for after, before in prerequisites:
            graph[before].append(after)
            indegree[after] += 1

        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        schedule = []
        while queue:
            course = queue.popleft()
            schedule.append(course)
            for nextCourse in graph[course]:
                indegree[nextCourse] -= 1
                if indegree[nextCourse] == 0:
                    queue.append(nextCourse)
        
        if len(schedule) == numCourses:
            return schedule
        else:
            return []