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


def solve():
    t  = num()
    for _ in range(t):
        n = num()
        graph = []
        for _ in range(n):
            li = list(string())
            graph.append(li)
        
        my_nums = [i for i in range(1, n+1)]

        def is_edge(num1, num2):
            num1-=1
            num2-=1

            if graph[num1][num2] == '1':
                return True
            
            return False
        

        
        for i in range(1, len(my_nums)):
            target_num = my_nums[i]

            j = i-1
            while j >= 0 and not is_edge(my_nums[j], target_num):
                my_nums[j+1] = my_nums[j]
                j-=1
            
            my_nums[j+1] = target_num
        
        print(*my_nums)
            
            
            # for j in range(i-1,-1, -1):
            #     if not is_edge(my_nums[i], target_num):
            #         my_nums[j+1] = my_nums[j]
                

                    # my_nums[i], my_nums[j] = my_nums[j], my_nums[i]
        
        # print(my_nums)

            
        
        # print(graph)
    






if __name__ == "__main__":
    solve()