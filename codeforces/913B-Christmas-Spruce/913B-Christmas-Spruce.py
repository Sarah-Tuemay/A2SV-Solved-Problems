from collections import defaultdict
n = int(input())
parents = set()
parents.add(1)
my_dict = defaultdict(list)
k = 2
for i in range(n-1):
    t = int(input())
    my_dict[t].append(k)
    parents.add(t)
    k+=1
possible = True
for key in my_dict:
    cnt = 0
    for i in range(len(my_dict[key])):
        if my_dict[key][i] not in parents:
            cnt+=1
    
    if cnt < 3:
        possible = False
        break

if possible:
    print("Yes")
else:
    print("No")