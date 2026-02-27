t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    left = 0
    right = 1
    ans = []
    ans.append(nums[0])

    while True:

        if nums[right] > nums[right-1]:
            while right < len(nums) and nums[right] > nums[right-1]:
                right += 1

            ans.append(nums[right-1])

        else:
            while right < len(nums) and nums[right] < nums[right-1]:
                right += 1
            ans.append(nums[right-1])
        
        if right == len(nums):
            break
        
    print(len(ans))
    print(" ".join(str(a) for a in ans))

