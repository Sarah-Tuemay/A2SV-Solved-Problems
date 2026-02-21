import sys
n, k = map(int,sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))


nums_dif = nums[len(nums)-1] - nums[0]
gaps = []

left = 0
right = 1
while right < len(nums):
    gaps.append(nums[right]-nums[left])
    left += 1
    right += 1

gaps.sort(reverse=True)

i = 0
while i < k-1:
    nums_dif -= gaps[i]
    i+=1
print(nums_dif)
