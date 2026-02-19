import math
n = int(input())

list1 = list(map(int, input().split()))

list1.sort()
if n % 2 == 0:
    midean = math.ceil(n//2) - 1
else:
    midean = math.ceil(n//2)


print(list1[midean])
