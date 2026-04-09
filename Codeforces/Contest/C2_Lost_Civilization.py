t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    stack = [arr[0]]

    res = 1

    listt = [1]

    for i in range(1,n):
        if arr[i] > arr[i-1] + 1:
            res += 1
            stack = [arr[i]]
        elif arr[i] == arr[i-1]:
            if arr[i] > stack[0]:
                stack.append(arr[i])
            else:
                stack = [arr[i]]
                res += 1
        elif arr[i] == arr[i-1] + 1:
            stack.append(arr[i])
        elif arr[i] < arr[i-1]:
            if arr[i] > stack[0]:
                stack.append(arr[i])
            else:
                stack = [arr[i]]
                res += 1
        else:
            stack = [arr[i]]
            res += 1
        listt.append(res)
    print(listt)

    count = 0
    for l in range(0, n):
        for r in range(l, n):
            if listt[r] > listt[l] and arr[r] >= arr[l]:
                count += listt[r] - listt[l] + 1
            else:
                
    print(count)

        

