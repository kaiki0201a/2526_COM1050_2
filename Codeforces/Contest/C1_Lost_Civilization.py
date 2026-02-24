t = int(input())

"""
- Dùng stack
- Danh gia voi cac TH
+ step > 1
+ step = 0, 1
+ step < 0:
    + Có thể nếu trước đó có số có thể tạo ra nó
"""
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    stack = [arr[0]]

    res = 1
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
    print(res)
        

