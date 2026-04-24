class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        N = len(graph)-1

        def dfs(node, path):
            path.append(node)

            if node == N:
                result.append(path[:])
                return

            for negh in graph[node]:
                dfs(negh, path)
                path.pop()
        
        dfs(0, [])

        return result
