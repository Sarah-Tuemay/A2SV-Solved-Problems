def merge_sort(arr):
    global possible
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    if not merge(left, right):
        possible = False
        return
    
    return merge(left, right)

def merge(left, right):
    swap = False
    lsize = len(left) if left else 0
    rsize = len(right) if right else 0
    global cnt
    result = []
    i = j = 0

    if left and right:
        if min(left) - max(right) != 1 and min(right) - max(left) != 1:
            # print(left, right)
            return False
    if left and right and right[0] - left[-1] != 1:
        # print(left, right)
        cnt += 1

    while i < lsize and j < rsize:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    if i < lsize: result.extend(left[i:])
    if j < rsize: result.extend(right[j:])

    return result

t = int(input())
for _ in range(t):
    possible = True
    cnt = 0
    n = int(input())
    nums = list(map(int, input().split()))
    merge_sort(nums)

    if not possible:
        print(-1)
    else:
        print(cnt//2)