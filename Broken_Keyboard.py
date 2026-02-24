t = int(input())

for _ in range(t):
    s = input()
    my_set = set()

    left = 0
    right = 1

    while left < len(s):
        if right >= len(s):
            my_set.add(s[left])
            left+=1
        elif s[left] == s[right]:
            # if s[left] in my_set:
            #     my_set.remove(s[left])
            left += 2
            right += 2
        else:
            my_set.add(s[left])
            
            left += 1
            right += 1

    my_list = list(my_set)
    my_list.sort()
    print("".join(list(my_list)))
