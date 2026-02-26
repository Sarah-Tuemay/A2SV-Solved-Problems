n, s = map(int, input().split())

nums = list(map(int, input().split()))
sum1 = 0
left = 0
ans = 0

for right in range(len(nums)):
    sum1 += nums[right]
    while sum1 >= s:
        ans += len(nums)-right
        sum1 -= nums[left]
        left += 1 


print(ans)
