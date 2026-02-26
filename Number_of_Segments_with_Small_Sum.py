n, s = map(int, input().split())

nums = list(map(int, input().split()))

left = 0
ans = 0
sum1 = 0
for right in range(len(nums)):
    sum1 += nums[right]

    while sum1 > s:
        sum1 -= nums[left]
        left+=1
    
    ans += right - left +1

print(ans)
