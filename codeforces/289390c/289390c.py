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
    n, m = nums()
    exprience = [0] * n
    root = [i for i in range(n)]
    size = [1] * n
    def find(x):
        while x != root[x]:
            x = root[x]
        
        return x

    def union(x, y):
        rootx = find(x)
        rooty = find(y)
        if rootx != rooty:
            if size[rooty] > size[rootx]:
                rootx, rooty = rooty, rootx
            root[rooty] = rootx
            size[rootx] += size[rooty]
            exprience[rooty] -= exprience[rootx]
    for _ in range(m):
        s  = string().split()

        if s[0] == 'add':
            x = find(int(s[1])-1)
            exprience[x] += int(s[2])
        elif s[0] == 'join':
            union(int(s[1])-1, int(s[2])-1)
        else:
            y = 0
            x = int(s[1])-1
            # print(exprience)
            while x != root[x]:
                y += exprience[x]
                x = root[x]
            y+=exprience[x]
            print(y)

if __name__ == "__main__":
    solve()