t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    ans = 0
    if "aa" in s:
        print(2)
    elif "aca" in s or "aba" in s:
        print(3)
    elif "acba" in s or "abca" in s:
        print(4)
    elif "accabba" in s or "abbacca" in s:
        print(7)
    else:
        print(-1)
      
