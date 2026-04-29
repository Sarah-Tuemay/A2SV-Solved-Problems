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

def solve():
    t = num()
    for _ in range(t):
        n = num()
        nums = lst()

        adj = [[] for _ in range(n)]
        incoming = [0 for _ in range(n)]
        

        for i in range(n):
            adj[i].append(nums[i]-1)
            incoming[nums[i]-1] += 1
        
        queue = deque()
        for i in range(n):
            if incoming[i] == 0:
                queue.append(i)
        
        pre_ = incoming.copy()
        ans = 0
        # print(adj)


        while queue:
            size_ = len(queue)
            ans+=1
            for i in range(size_):
                node = queue.popleft()
                for negh in adj[node]:
                    incoming[negh] -= 1
                    if incoming[negh] == 0:
                        queue.append(negh)
        
        
        print(ans+2)
        
    




if __name__ == "__main__":
    solve()