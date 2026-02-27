from collections import defaultdict
from sys import stdin
n, k = map(int, stdin.readline().split())

nums = list(map(int, stdin.readline().split()))

left = 0
max_ = float('-inf')
ans = []
my_dict = defaultdict(int)

for right in range(n):
    my_dict[nums[right]] += 1

    while len(my_dict) > k:
        my_dict[nums[left]] -= 1
        if my_dict[nums[left]] == 0:
            del my_dict[nums[left]]
        left += 1


    if right - left > max_:
        ans = [left+1, right+1]
        max_ = right - left
    


print(" ".join(str(a) for a in ans))
