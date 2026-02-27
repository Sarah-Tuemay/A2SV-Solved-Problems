from collections import defaultdict
n, k = map(int, input().split())
nums = list(map(int, input().split()))
my_dict = defaultdict(int)
left = 0
ans = 0

for right in range(len(nums)):
    my_dict[nums[right]] += 1

    while len(my_dict) > k:
        my_dict[nums[left]]-=1
        if my_dict[nums[left]] == 0:
            del my_dict[nums[left]]
    
        left +=1
    
    ans += right-left+1

print(ans)
