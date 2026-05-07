import sys
import math
import random
# sys.setrecursionlimit(200000)

from itertools import accumulate
from bisect import bisect_left, bisect_right
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush


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
    tasks = []
    for _ in range(t):
        s = string()
        s = tuple(s.split(' '))
        tasks.append(s)
        heapp = []
        heapify(heapp)
    
    ans = []
    for task in tasks:
        if task[0] == "insert":
            heappush(heapp, int(task[1]))
            ans.append(f"insert {task[1]}")
        elif task[0] == "removeMin":
            if heapp:
                heappop(heapp)
            else:
                ans.append("insert 0")
            ans.append("removeMin")
        elif task[0] == "getMin":
            if heapp and int(task[1]) < heapp[0]:
                heappush(heapp, int(task[1]))
                ans.append(f"insert {task[1]}")
                ans.append(f"getMin {task[1]}")
            elif heapp and int(task[1]) == heapp[0]:
                ans.append(f"getMin {task[1]}")
              
            else:
                while heapp and heapp[0] < int(task[1]):
                    min_ = heappop(heapp)
                    ans.append("removeMin")

                
                if heapp and heapp[0] == int(task[1]):
                    ans.append(f"getMin {task[1]}")

                else:
                    heappush(heapp, int(task[1]))
                    ans.append(f"insert {task[1]}")
                    ans.append(f"getMin {task[1]}")
        
    print(len(ans))

    for i in range(len(ans)):
        print(ans[i])


if __name__ == "__main__":
    solve()