import math


def main():
    n, x, k = map(int, input().split())
    s = input()
    num_zeros = 0
    second_round = []

    j = 0 
    i = 0
    while j < len(s):
        if s[j] == "L":
            x -= 1
        else:
            x += 1
           
        i+=1
        if x == 0:
            num_zeros += 1
            break
        if i == k:
            print(num_zeros)
            return   
        j+=1              
    if j == len(s):
        print(num_zeros)
        return 
    j = 0
    while j < len(s):
        if s[j] == "L":
            x -= 1
            second_round.append(x)
        else:
            x += 1
            second_round.append(x)
        i += 1
       
        if x == 0:
            num_zeros += 1
            break
        if i == k:
            print(num_zeros)
            return 
        
        j += 1
        
    if j == len(s):
        print(num_zeros)
        return 

    num_zeros += (k-i) // len(second_round)
    print(num_zeros)
    return
t = int(input())

for i in range(t):
    main()
