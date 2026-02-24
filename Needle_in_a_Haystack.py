from collections import Counter
test_cases = int(input())
for _ in range(test_cases):
    s = input()
    t = input()

    s_count = Counter(s)
    t_count = Counter(t)

    found = False

    for key in s_count:
        if key not in t_count or t_count[key] < s_count[key]:
            found = True
            break

        t_count[key] -= s_count[key]

        if t_count[key] == 0:
            del t_count[key]
    
    if found:
        print("Impossible")
        continue
    ans = ""
    t_count = dict(sorted(t_count.items()))
    t = ""
    for key in t_count:
        t += key * t_count[key]
    

    s_pointer = 0
    t_pointer = 0

    while s_pointer < len(s) and t_pointer < len(t):
        if s[s_pointer] <= t[t_pointer]:
            ans += s[s_pointer]
            s_pointer += 1
        else:
            ans += t[t_pointer]
            t_pointer += 1
    
    while s_pointer < len(s):
        ans += s[s_pointer]
        s_pointer += 1
    
    while t_pointer < len(t):
        ans += t[t_pointer]
        t_pointer += 1
    
    print(ans)
