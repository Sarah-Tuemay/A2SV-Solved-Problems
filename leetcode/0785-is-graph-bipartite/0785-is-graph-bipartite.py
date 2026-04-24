class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1 for _ in range(len(graph))]
        def dfs(node, graph):
            temp = True
            for negh in graph[node]:
                if color[negh] == -1:
                    if color[node] == 0:
                        color[negh] = 1
                    else:
                        color[negh] = 0

                    temp = temp and dfs(negh, graph)
                elif color[negh] == color[node]:
                    return False
            
            return temp
        color =[-1 for _ in range(len(graph))]
        result = True

        for node in range(len(graph)):
            if color[node] == -1:
                color[node] = 0
                result = result and dfs(node, graph)
            
        return result
        

        # def dfs(node):
        #     for negh in graph[node]:
        #         if color[negh] == -1:
        #             if color[node] == 0:
        #                 color[negh] = 1
        #             else:
        #                 color[negh] = 0             
        #             dfs(negh)
        #         elif color[negh] == color[node]:
        #             return False
            
        #     return True

        
        # for node in range(len(graph)):
        #     if color[node] == -1:
        #         color[node] = 0
        #         res = dfs(node)
        #         if not res:
        #             return False
                
        # return True
