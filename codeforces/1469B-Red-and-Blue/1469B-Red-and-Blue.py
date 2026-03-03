t = int(input())
for i in range(t):
    n= int(input())
    red_nums = list(map(int, input().split()))
    m = int(input())
    blue_nums = list(map(int, input().split()))

    rd_pre = 0
    bl_pre = 0
    maxr = 0
    maxb = 0
    
    for i in range(n):
        rd_pre += red_nums[i]
        maxr = max(maxr, rd_pre)


    for i in range(m):
        bl_pre += blue_nums[i]
        maxb = max(maxb, bl_pre)
        
    
    print(maxr+maxb)