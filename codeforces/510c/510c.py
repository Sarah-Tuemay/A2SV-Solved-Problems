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
    n = num()
    li = []
    adj = [[] for _ in range(26)]
    incoming = [0 for _ in range(26)]
    for _ in range(n):
        s = string()
        li.append(s)
    
    # print(li)
    for i in range(n-1):
        for j in range(len(li[i])):
            if j == len(li[i+1]):
                print("Impossible")
                exit()
            if li[i][j] != li[i+1][j]:
                a = ord(li[i+1][j]) - ord('a')
                b = ord(li[i][j]) - ord('a')
                adj[b].append(a)
                incoming[a] += 1
                break
    
    queue = deque()

    for i in range(26):
        if incoming[i] == 0:
            queue.append(i)

    
    ans = []

    while queue:
        node = queue.popleft()
        ans.append(chr(node+ord('a')))

        for negh in adj[node]:
            incoming[negh]-=1

            if incoming[negh] == 0:
                queue.append(negh)
    
    # print(len(ans), "".join(ans))
    if len(ans) < 26:
        print("Impossible")
    else:
        print("".join(ans))




    # print(adj) 


    adj = [[] for i in range(26)]





if __name__ == "__main__":
    solve()