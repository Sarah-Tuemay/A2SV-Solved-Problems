import sys
import math
import random
# sys.setrecursionlimit(200000)

from itertools import accumulate
from bisect import bisect_left, bisect_right
from collections import defaultdict, Counter, deque

input = sys.stdin.readline

INF = float('inf')
MOD = 10**9 + 7
XOR = random.randint(1, 10 ** 7)

def num(): return int(input())
def lst(): return list(map(int, input().split()))
def nums(): return tuple(map(int, input().split()))
def string(): return input().strip() 
def directions(): return [(0,1),(0,-1),(-1,0),(1,0)]

def graph_bfs(s_node, graph):
    n = len(graph)
    visited = [False] * n
    q = deque()
    q.append((s_node, 0))
    visited[s_node] = True

    max_dist = 0
    furthest_node = s_node

    while q:
        node, dist = q.popleft()
        if dist > max_dist:
            max_dist = dist
            furthest_node = node
        
        for negh in graph[node]:
            if not visited[negh]:
                visited[negh] = True
                q.append((negh, dist+1))
    
    return furthest_node, max_dist


def solve():
    n = num()
    graph = [[] for i in range(n)]
    for _ in range(n-1):
        u, v = nums()
        u-=1
        v-=1
        graph[u].append(v)
        graph[v].append(u)

    dist1 = graph_bfs(0,graph)
    dist2 = graph_bfs(dist1[0], graph)
    print(dist2[1] *3)


if __name__ == "__main__":
    solve()