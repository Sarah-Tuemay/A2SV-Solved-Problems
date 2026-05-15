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

def find(x, root):
    while x != root[x]:
        root[x] = root[root[x]]
        x = root[x]
    
    return root[x]

def union(x, y, root):
    rootx = find(x, root)
    rooty = find(y, root)

    if rootx != rooty:
        root[rootx] = rooty
    

def solve():
    t = num()
    for _ in range(t):
        n, m1, m2 = nums()
        rootF = [i for i in range(n)]
        rootG = [i for i in range(n)]
        opF = []
        opG = []

        for _ in range(m1):
            a, b = nums()
            opF.append((a-1, b-1))
        
        for _ in range(m2):
            a,b = nums()
            opG.append((a-1, b-1))
            union(a-1, b-1, rootG)
        

        ans = 0

        for a, b in opF:
            if find(a, rootG) != find(b, rootG):
                ans+=1
            else:
                union(a, b, rootF)
        
        for a, b in opG:
            if find(a, rootF) != find(b, rootF):
                ans +=1
                union(a,b, rootF)
        
        print(ans)
        




if __name__ == "__main__":
    solve()