t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    res = -float("inf")
    count = 0
    for i in arr:
        if i > res:
            res = i
            count = 1
        elif i == res:
            count += 1
    print(count)