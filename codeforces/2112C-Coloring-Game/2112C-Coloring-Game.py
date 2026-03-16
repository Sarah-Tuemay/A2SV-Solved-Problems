t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    a.sort()
    M = a[-1] # maximum element
    ans = 0
    for i in range(2, n):
        z = a[i] 
        T = max(z, M - z)

        l = 0
        r = i - 1

        while l < r:
            if a[l] + a[r] > T:
                ans += r - l
                r -= 1
            else:
                l += 1

    print(ans)