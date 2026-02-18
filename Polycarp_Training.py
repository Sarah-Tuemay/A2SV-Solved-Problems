n = int(input())
nums = list(map(int, input().split()))

ans = 0
day = 1
nums.sort()

for i in range(len(nums)):
    if nums[i] >= day:
        ans += 1
        day+=1

print(ans)
