from bisect import bisect_left
t = int(input())

def getIdx(val):
    return bisect_left(b, val)
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    b.sort()
    a[0] = min(a[0], b[0]-a[0])
    flag = 1

    if a == sorted(a):
        print("YES")
        continue

    for i in range(1, len(a)):
        index = getIdx(a[i]+a[i-1])

        if index == m and a[i] < a[i-1]:
            flag = 0
            break

        if index == m:
            continue

        if a[i] >= a[i-1]:
            a[i] = min(a[i], b[index]-a[i])
        else:
            a[i] = b[index] - a[i]
    
    if flag:
        print("YES")
    else:
        print("NO")