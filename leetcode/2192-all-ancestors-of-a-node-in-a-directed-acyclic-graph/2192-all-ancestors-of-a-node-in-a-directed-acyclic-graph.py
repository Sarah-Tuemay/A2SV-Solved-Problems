class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = [[] for _ in range(n)]
        incoming = [0 for _ in range(n)]
        my_dict = defaultdict(set)
        for fromi, toi in edges:
            adj[fromi].append(toi)
            incoming[toi]+=1
        

        # print(adj)
        queue = deque()
        ans = [[] for _ in range(n)]
        for i in range(n):
            if incoming[i] == 0:
                queue.append(i)
            
        while queue:
            node = queue.popleft()
            for negh in adj[node]:
                my_dict[negh].update(my_dict[node])
                my_dict[negh].add(node)
                incoming[negh]-=1

                if incoming[negh] == 0:
                    queue.append(negh)
        
        ans = [[] for _ in range(n)]

        for key in my_dict:
            ans[key] = sorted(list(my_dict[key]))
        
        return ans
        


