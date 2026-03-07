import sys
input = sys.stdin.readline


n, k, q = map(int, input().split())


rec = [0] * 200005

for i in range(n):
    l, r = map(int, input().split())
    rec[l] += 1
    rec[r+1] -= 1


sum1 = 0
pre_sum = [0] * 200005
for i in range(1, 200001):
    sum1 += rec[i]
    pre_sum[i] = sum1


admissible = [0] * 200005
for i in range(1, 200001):
    if pre_sum[i] >= k:
        admissible[i] = 1
    else:
        admissible[i] = 0


pre_sum1 = [0] * 200005
sum2 = 0
for i in range(1, 200001):
    sum2 += admissible[i]
    pre_sum1[i] = sum2

ans_list = []
for i in range(q):
    a, b = map(int, input().split())
    ans = pre_sum1[b] - pre_sum1[a-1]
    print(ans)