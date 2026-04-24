class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        N = len(bombs)
        graph =[[] for _ in range(N)]
        for i in range(N):
            for j in range(i+1,N):
                x1, y1,r1 = bombs[i]
                x2,y2,r2 = bombs[j]


                d =sqrt(((x1-x2)**2) +((y1-y2)**2) )
                # print(bombs[i], bombs[j],d)
                if d <= r1: graph[i].append(j)
                if d <= r2: graph[j].append(i)
        
        max_ = 0

        print(graph)
        def dfs(node):
            nonlocal cnt
            visited.add(node)
            cnt+=1
            for negh in graph[node]:
                if negh not in visited:
                    dfs(negh)

        for node in range(len(graph)):
            cnt = 1
            visited = set()
            visited.add(node)
            for negh in graph[node]:
                if negh not in visited:
                    dfs(negh)
            
            max_ = max(max_, cnt)
        
        return max_



