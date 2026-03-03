from sys import stdin
from collections import Counter

t = int(stdin.readline())
for _ in range(t):
    n, l, r = map(int, stdin.readline().split())
    all_s = list(map(int, stdin.readline().split()))

    left_c = Counter(all_s[:l])
    right_c = Counter(all_s[l:])

    for sock in left_c:
        if sock in right_c:
            m = min(left_c[sock], right_c[sock])
            left_c[sock] -= m
            right_c[sock] -= m
    
    l_rem = sum(left_c.values())
    r_rem = sum(right_c.values())


    if r_rem > l_rem:
        left_c, right_c = right_c, left_c
        l_rem, r_rem = r_rem, l_rem
    
    ans = 0
    
    diff = (l_rem - r_rem) // 2

    for sock in left_c:

        can_pair = left_c[sock] // 2
        take = min(can_pair, diff)
        
        ans += take
        l_rem -= take * 2
        diff -= take


    ans += (diff * 2) + r_rem
    print(ans)