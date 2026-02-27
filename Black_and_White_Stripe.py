from collections import defaultdict
t = int(input())

for _ in range(t):
    n, k = map(int,input().split())
    s = input()
    min_ = float('inf')
    left = 0
    my_dict = defaultdict(int)
    if 'B' * k in s:
        print(0)
        continue

    for right in range(n):
        my_dict[s[right]] += 1

        while my_dict["B"] + my_dict["W"] == k:
            min_ = min(min_,my_dict["W"])
            my_dict[s[left]] -= 1
            left += 1
    
    print(min_)
