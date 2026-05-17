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
    n, m, k = nums()
    root = [i for i in range(n)]
    seen = set()
    def find(x):
        while x != root[x]:
            root[x] = root[root[x]]
            x = root[x]
        return root[x]
    
    def union(x, y):
        rootx = find(x)
        rooty = find(y)
        if rootx != rooty:
            root[rootx] = rooty

    for _ in range(m):
        a, b = nums()
        seen.add((a-1, b-1))
        seen.add((b-1,a-1))
    
    op = []
    for i in range(k):
        s = string()
        op.append(s.split(' '))
    
    for i in range(k):
        o, a, b = op[i]
        if o == 'cut':
            seen.remove((int(a)-1, int(b)-1))
            seen.remove((int(b)-1, int(a)-1))
    
    for a, b in seen:
        union(a, b)
    
    op.reverse()

    ans = []

    for i in range(k):
        o, a, b = op[i]

        if o == 'ask':
            if find(int(a)-1) == find(int(b)-1):
                ans.append('YES')
            else:
                ans.append('NO')
        else:
            union(int(a)-1, int(b)-1)
    
    print("\n".join(ans[::-1]))


    




if __name__ == "__main__":
    solve()