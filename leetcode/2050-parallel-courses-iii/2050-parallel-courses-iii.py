class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        N = len(time)
        completion_time = [time[i] for i in range(N)]
        indegree = [0 for i in range(N)]
        adj = [[] for i in range(N)]

        total_time = 0

        for pre, course in relations:
            adj[pre-1].append(course-1)
            indegree[course-1] += 1
        
        queue = deque()
        for i in range(N):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            total_time += completion_time[node]

            for negh in adj[node]:
                indegree[negh] -= 1
                completion_time[negh] = max(completion_time[negh],completion_time[node]+time[negh])

                if indegree[negh] == 0:
                    queue.append(negh)
        
        return max(completion_time)
        