class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(set)
        for before, after in prerequisites:
            graph[before].add(after)

        def recurse(start, target):
            queue = deque([start])
            seen = set([start])
            while queue:
                course = queue.popleft()
                if course == target:
                    return True
                for nextCourse in graph.get(course, ()):
                    if nextCourse not in seen:
                        seen.add(nextCourse)
                        queue.append(nextCourse)
            
            return False

        output = []
        for u, v in queries:
            output.append(recurse(u, v))

        return output