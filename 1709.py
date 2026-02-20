t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    num_op = 0
    operations = []

    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                num_op+=1
                operations.append([1, j+1])

    for i in range(len(b)):
        for j in range(len(b)-i-1):
            if b[j] > b[j+1]:
                b[j], b[j+1] = b[j+1], b[j]
                num_op+=1
                operations.append([2, j+1])

    for i in range(len(a)):
        if a[i] > b[i]:
            a[i], b[i] = b[i], a[i]
            num_op+=1
            operations.append([3, i+1])

    print(num_op)
    for i in range(len(operations)):
        print(operations[i][0], operations[i][1])
