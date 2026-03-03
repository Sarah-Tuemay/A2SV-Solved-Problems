t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    b = input()

    arr = []
    c_zero = 0
    c_one = 0

    for i in range(len(s)):
        if s[i] == "0":
            c_zero+=1
        else:
            c_one +=1
        
        arr.append([c_zero, c_one])

        flip = 0
    
    for i in range(len(s)-1, -1,-1):

        if flip % 2 == 0:
            if s[i] != b[i]:
                if arr[i][0] != arr[i][1]:
                    print("NO")
                    break
                else:
                    flip+=1
        
        else:
            if s[i] == b[i]:
                if arr[i][0] != arr[i][1]:
                    print("NO")
                    break
                else:
                    flip+=1
    
    else:
        print("YES")