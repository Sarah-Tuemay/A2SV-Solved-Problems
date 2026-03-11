s = input()

stack = []
max_ = 0
cnt = 0
cnt_br = 0
my_list = [0] * len(s)

for i in range(len(s)):
    if s[i] == ")":
        if stack and s[stack[-1]] == "(":
            my_list[stack[-1]] = 1
            stack.pop()
            my_list[i] = 1
    else:
        stack.append(i)


max_ = 0
sum1 = 0
cnt = 0
for i in range(len(my_list)):
    if my_list[i] == 0:
        sum1 = 0
    else:
        sum1 += 1

    if sum1 > max_:
        cnt = 1
        max_ = sum1
    elif sum1 == max_:
        cnt += 1
if max_ == 0:
    print(0,1)
else:
    print(max_, cnt)