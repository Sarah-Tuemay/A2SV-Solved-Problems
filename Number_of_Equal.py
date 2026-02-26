from collections import Counter
a , b = map(int, input().split())

a_nums = list(map(int, input().split()))
b_nums = list(map(int, input().split()))

b_nums_count = Counter(b_nums)

ans = 0
for num in a_nums:
    if num in b_nums_count:
        ans += b_nums_count[num]

print(ans)
